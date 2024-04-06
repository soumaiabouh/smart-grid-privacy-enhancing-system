import csv
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class SmartMeter:
    def __init__(self, pes_public_key, filename):
        self.pes_public_key = RSA.import_key(pes_public_key)
        self.encrypted_data_list = []
        self._load_data(filename)
        self.id = self._generate_id()
        self.aes_key = self._generate_key()
        
    def _load_data(self, filename):
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for i, row in enumerate(reader):
                    if i >= 4320:  # Stop after 4,320 rows
                        break
                    timestamp, reading = row[0], row[1]
                    self._encrypt_data_and_store(timestamp, reading)  # Encrypt each reading with its timestamp
        except FileNotFoundError:
            print(f"The file {filename} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
    def _generate_key(self):
        # Generate a random 256-bit key
        return get_random_bytes(32)
    
    def _generate_id(self):
        # generate id and return it
        return get_random_bytes(16)
        
    def _encrypt_data_and_store(self, timestamp, reading):        
        cipher_aes = AES.new(self.aes_key, AES.MODE_GCM) # Important to generate a new cipher everytime for security reasons
        encrypted_data, tag = cipher_aes.encrypt_and_digest(reading.encode('utf-8')) # Encrypt data using AES-GCM and converting string to bytes
        nonce = cipher_aes.nonce # Nonce is needed for decryption in GCM mode
        
        self.encrypted_data_list.append({
            'timestamp': timestamp,
            'encrypted_data': encrypted_data,
            'nonce': nonce,
            'tag': tag
        })
        
    def get_encrypted_data(self):
        # public function, return self.data_dict
        return self.encrypted_data_list
            
    def _encrypt_aes_key(self):
        # function that encrypts using RSA the smart meter AES key using a public key 
        cipher_rsa = PKCS1_OAEP.new(self.pes_public_key)
        encrypted_key = cipher_rsa.encrypt(self.aes_key)
        return encrypted_key


