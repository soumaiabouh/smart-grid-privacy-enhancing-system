from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from phe import paillier
from tqdm import tqdm


class PES:
    def __init__(self, key_size=2048, aes_key_size=16):
        self.rsa_key_pair = RSA.generate(key_size)
        self.rsa_public_key = self.rsa_key_pair.publickey().export_key()

        self.pallier_public_key, self.pallier_private_key = paillier.generate_paillier_keypair()

        # TODO: make the MDMS manager generate the key instead 
        self.aes_key = get_random_bytes(aes_key_size)  # AES key for re-encryption

        self.pallier_encrypted_data_list = []  # Store Paillier encrypted data ()

    def get_public_key(self):
        # The public key will be used by the smart meters to encrypt their AES key
        return self.rsa_public_key

    def _decrypt_data(self, encrypted_aes_key, data_list):
        # Decrypt the AES key
        cipher_rsa = PKCS1_OAEP.new(self.rsa_key_pair)  # Creates a new RSA cipher object for decryption
        aes_key = cipher_rsa.decrypt(encrypted_aes_key)

        # Decrypt each piece of reading and store it
        decrypted_data_list = []

        for data in data_list:
            # Format of data: {timestamp, encrypted_data, tag, nonce}
            cipher_aes = AES.new(aes_key, AES.MODE_GCM, nonce=data['nonce'])
            decrypted_data = cipher_aes.decrypt_and_verify(data['encrypted_data'], data['tag'])

            decrypted_data_info = {"timestamp": data["timestamp"],
                                   "decrypted_data": decrypted_data}

            decrypted_data_list.append(decrypted_data_info)

        return decrypted_data_list

    def _pallier_encrypt_and_store(self, decrypted_data_list):
        # Wrap the loop with tqdm for a progress bar
        for reading in tqdm(decrypted_data_list, desc="Encrypting"):
            encrypted_data = self.pallier_public_key.encrypt(float(reading["decrypted_data"].decode('utf-8')))

            encrypted_data_info = {
                "timestamp": reading["timestamp"],
                "encrypted_data": encrypted_data
            }

            self.pallier_encrypted_data_list.append(encrypted_data_info)

    def _aggregate_data(self):
        # Ensure there is data to aggregate
        if len(self.pallier_encrypted_data_list) == 0:
            print("No data to aggregate.")
            return None

        # Initialize aggregation with the encrypted value of 0
        # This is important for cases where the list might be empty, avoiding undefined behavior
        zero_encrypted = self.pallier_public_key.encrypt(0)
        aggregated_encrypted = zero_encrypted

        # Perform homomorphic addition for all items
        for reading in self.pallier_encrypted_data_list:
            aggregated_encrypted += reading["encrypted_data"]

        return aggregated_encrypted

    def _aes_encrypt_aggregate(self, aggregate, timestamp):
        cipher_aes = AES.new(self.aes_key, AES.MODE_GCM)  # Generate new cipher
        decrypted_aggregate = self.pallier_private_key.decrypt(aggregate)  # First decrypt the value

        combined_data = f"{timestamp}, {decrypted_aggregate}".encode('utf-8')

        encrypted_data, tag = cipher_aes.encrypt_and_digest(combined_data)
        nonce = cipher_aes.nonce
        return {'encrypted_data': encrypted_data, 'nonce': nonce, 'tag': tag}

    # Main method, we call everything here - separation of concerns 
    def aggregate_and_encrypt(self, encrypted_aes_key, data_list, start_index=0):
        # Filter data_list to start from the given index
        filtered_data_list = data_list[start_index:]
        
        # First we decrypt the Smart meter AES encrypted data, and we directly encrypt the data using Pallier 
        self._pallier_encrypt_and_store(self._decrypt_data(encrypted_aes_key, filtered_data_list))

        timestamp = self.pallier_encrypted_data_list[0]["timestamp"]  # Keeping the first timestamp

        # Next we aggregate the data -> Assuming we're only sent the exact number of readings we want to aggregate
        paillier_encrypted_aggregate = self._aggregate_data()

        # Then, we decrypt and reencrypt the data         
        aes_encrypted_aggregate = self._aes_encrypt_aggregate(paillier_encrypted_aggregate, timestamp)

        # Cleaning up (we don't want to keep the data for longer than needed)
        self.pallier_encrypted_data_list.clear()

        return aes_encrypted_aggregate