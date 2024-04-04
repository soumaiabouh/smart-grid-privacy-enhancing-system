from Crypto.Cipher import AES
import os

class SmartMeter:
    def __init__(self, dataCSV):
        self.data_dict = self.load_data(dataCSV)
        self.generate_id()
        self.generate_key()
        
    def load_data(self, filename):
        # load file, get data as dict, encrypt it using encrypt_data() and return it
        pass
        
    def generate_key(self):
        # Generate a random 256-bit key
        self.key = get_random_bytes(32)

    def generate_id(self):
        # generate id and return it
        self.id = get_random_bytes(32)
        
    def encrypt_data(self, data):
        # helper function for load_data, takes the data and encrypts it using AES
        # helper function for load_data, takes the data and encrypts it using AES
        cipher = AES.new(self.key, AES.MODE_CTR) # new object
        ciphertext = cipher.encrypt(data) # encrypt plaintext 
        return ciphertext, cipher.nonce # return cipher and nonce
        
    def get_encrypted_data(self):
        # public function, return self.data_dict
        return self.data_dict
            
    def getKey(self):
        # return key. This must only be called once by the UCS and once by the DataConcentrator.
        return self.key
