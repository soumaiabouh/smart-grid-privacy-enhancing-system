from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from pymongo import MongoClient
from bson import ObjectId
import base64


class MdmsManager:
    def __init__(self, key_size=2048, 
                 database_url = "mongodb+srv://soumsoumbouh07:Apple100@smartmeters.k0koxzq.mongodb.net/", 
                 database_name = "smart_meter_readings", 
                 collection_name = "demo"):
        self.rsa_key_pair = RSA.generate(key_size)
        self.rsa_public_key = self.rsa_key_pair.publickey().export_key()
        
        self.aggregated_data_dict = {}  # Dictionary to store aggregated data
        self.decrypted_data_dict = {}
        
        # MongoDB setup
        self.client = MongoClient(database_url)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]
    
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

      
    def send_data_to_mdms(self, aggregated_data: dict):
        # Insert aggregated data into MongoDB
        for id, data in aggregated_data.items():
            post = {"id": id, "data": data}
            self.collection.insert_one(post)
    
    def get_all_data(self):
        # Fetch all documents in the collection
        results = self.collection.find({})
        return list(results)

    def print_all_data(self):
        # Retrieve all data from the database
        all_data = self.get_all_data()
        # Iterate through each document and print the data
        for document in all_data:
            print(f"ID: {document['_id']}")
            data_entries = document['data']
            for entry in data_entries:
                # Since we have binary data from MongoDB, no need for base64 decoding
                encrypted_data = entry  # Already a bytes object
                print(encrypted_data)