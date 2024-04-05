from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class SmartMeter:
    def __init__(self, dataCSV):
        self.data_dict = self.load_data(dataCSV)
        self.generate_id()
        self.generate_keys()
        
    def load_data(self, filename):
        # load file, get data as dict, encrypt it using encrypt_data() and return it
        pass
        
    def generate_keys(self):
        # Generate a random 256-bit key
        self._key = get_random_bytes(32)
        
        # Generate key pair 
        self.key_pair = RSA.generate(2048)

    def generate_id(self):
        # generate id and return it
        self.id = get_random_bytes(32)
        
    def encrypt_data(self, data):
        # helper function for load_data, takes the data and encrypts it using AES
        cipher = AES.new(self._key, AES.MODE_GCM) # new object
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
