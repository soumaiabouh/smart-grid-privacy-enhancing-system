import csv
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class SmartMeter:
    def __init__(self, pes_public_key, dataCSV):
        self.pes_public_key = RSA.import_key(pes_public_key)
        self.data_dict = self.load_data(dataCSV)
        self.id = self.generate_id()
        self.aes_key = self.generate_key()
        
    def load_data(self, filename):
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for i, row in enumerate(reader):
                    if i >= 4320:  # Stop after 4,320 rows
                        break
                    timestamp, reading = row[0], row[1]
                    self.encrypt_data_and_store(timestamp, reading)  # Encrypt each reading with its timestamp
        except FileNotFoundError:
            print(f"The file {filename} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
    def generate_key(self):
        # Generate a random 256-bit key
        return get_random_bytes(32)
    
    def generate_id(self):
        # generate id and return it
        return get_random_bytes(16)
        
    def encrypt_data(self, data):
        # helper function for load_data, takes the data and encrypts it using AES
        cipher = AES.new(self.aes_key, AES.MODE_GCM) # new object
        ciphertext, tag = cipher.encrypt_and_digest(data) # encrypt plaintext 
        return ciphertext, tag, cipher.nonce # return cipher and nonce
        
    def get_encrypted_data(self):
        # public function, return self.data_dict
        return self.data_dict
            
    def get_key(self, public_key):
        # function that encrypts (RSA) smart meter key using a public key 
        cipher_rsa = PKCS1_OAEP.new(public_key)
        encrypted_key = cipher_rsa.encrypt(self._key)
        return encrypted_key


