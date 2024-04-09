from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


class MdmsManager:
    def __init__(self, key_size=2048):
        self.rsa_key_pair = RSA.generate(key_size)
        self.rsa_public_key = self.rsa_key_pair.publickey().export_key()
        
        self.aggregated_data_dict = {}  # Dictionary to store aggregated data
        self.decrypted_data_dict = {}
    
    def get_public_key(self):
        # The public key will be used by the PES to encrypt the aggregates
        return self.rsa_public_key
    
    def _decrypt_data(self, aggregated_data: dict):
        cipher_rsa = PKCS1_OAEP.new(self.rsa_key_pair)  # Initialize the RSA cipher with the private key
        
        for id, encrypted_aggregates in aggregated_data.items():
            # Check if the ID already exists in the decrypted data dictionary
            if id not in self.decrypted_data_dict:
                self.decrypted_data_dict[id] = []  # If not, initialize an empty list
                
            for encrypted_data in encrypted_aggregates:
                # Decrypt each encrypted aggregate using the RSA private key
                decrypted_data = cipher_rsa.decrypt(encrypted_data)
                # Assuming the decrypted_data is bytes, convert it to a string or the desired format as necessary
                # Append the decrypted data to the list for the corresponding ID
                self.decrypted_data_dict[id].append(decrypted_data)
        