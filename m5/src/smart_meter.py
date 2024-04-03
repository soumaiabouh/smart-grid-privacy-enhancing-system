from Crypto.Cipher import AES
import os

class SmartMeter:
    def __init__(self, dataCSV):
        self.data_dict = self.load_data(dataCSV)
        self.id = self.generate_id()
        
    def load_data(self, filename):
        # load file, get data as dict, encrypt it using encrypt_data() and return it
        pass
        
    def generate_id(self):
        # generate id and return it
        pass
        
    def encrypt_data(self):
        # helper function for load_data, takes the data and encrypts it using AES
        pass
        
    def get_encrypted_data(self):
        # public function, return self.data_dict
        pass
            
    def getKey(self):
        # return key. This must only be called once by the UCS and once by the DataConcentrator.
        pass
