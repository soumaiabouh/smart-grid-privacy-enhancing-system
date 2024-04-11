from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from pymongo import MongoClient
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

class MdmsManager:
    def __init__(self, key_size=2048, 
                 database_url = "mongodb+srv://soumsoumbouh07:Apple100@smartmeters.k0koxzq.mongodb.net/", 
                 database_name = "smart_meter_readings", 
                 collection_name = "demo"):
        
        self.rsa_key_pair = RSA.generate(key_size)
        self.rsa_public_key = self.rsa_key_pair.publickey().export_key()
        self.aggregated_data_dict = {}  # Dictionary to store aggregated data
        
        # MongoDB setup
        self.client = MongoClient(database_url)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]
    
    def get_public_key(self):
        # The public key will be used by the PES to encrypt the aggregates
        return self.rsa_public_key
    
    def _decrypt_data(self, aggregated_data: dict):
        cipher_rsa = PKCS1_OAEP.new(self.rsa_key_pair)  # Initialize the RSA cipher with the private key
        decrypted_data_dict = {}
        
        for id, encrypted_aggregates in aggregated_data.items():
            # Check if the ID already exists in the decrypted data dictionary
            if id not in decrypted_data_dict:
                self.decrypted_data_dict[id] = []  # If not, initialize an empty list
                
            for encrypted_data in encrypted_aggregates:
                # Decrypt each encrypted aggregate using the RSA private key
                decrypted_data = cipher_rsa.decrypt(encrypted_data)
                # Assuming the decrypted_data is bytes, convert it to a string or the desired format as necessary
                # Append the decrypted data to the list for the corresponding ID
                decrypted_data_dict[id].append(decrypted_data)
        
        return decrypted_data_dict
         
    def send_data_to_mdms(self, encrypted_aggregated_data: dict):
        # Insert aggregated data into MongoDB
        for id, data in encrypted_aggregated_data.items():
            post = {"id": id, "data": data}
            self.collection.insert_one(post)
             
    def calculate_smart_meter_total_energy_consumption(self, sm_id):
        # Retrieve all data from the database
        encrypted_data_records = self.collection.find({})
        
        total_consumption = 0.0
        cipher_rsa = PKCS1_OAEP.new(self.rsa_key_pair)

        # Iterate through each document to find the matching sm_id
        for record in encrypted_data_records:
            # Convert MongoDB Binary to bytes for comparison
            record_id_bytes = record['id']
            # Compare with the sm_id we're looking for
            if record_id_bytes == sm_id:
                for encrypted_data in record['data']:
                    # Decrypt each encrypted aggregate using the RSA private key
                    decrypted_data = cipher_rsa.decrypt(encrypted_data)
                    # Assuming the decrypted_data is bytes, convert it to a string
                    decrypted_string = decrypted_data.decode('utf-8')
                    # Split the string by comma and extract the reading value
                    timestamp, reading = decrypted_string.split(', ')
                    # Convert the reading to float and add it to the total consumption
                    total_consumption += float(reading)

        # Return the total consumption
        return total_consumption
    
    def delete_all_records(self):
        # This will delete all documents in the collection
        self.collection.delete_many({})
    
    def calculate_neighborhood_daily_consumption(self):
        # Initialize a dictionary to hold daily total consumption (key: day, value: total consumption)
        daily_consumption = {}
        
        encrypted_data_records = self.collection.find({})
        cipher_rsa = PKCS1_OAEP.new(self.rsa_key_pair)
        
        for record in encrypted_data_records:
            for encrypted_data in record['data']:
                decrypted_data = cipher_rsa.decrypt(encrypted_data)
                decrypted_string = decrypted_data.decode('utf-8')
                timestamp, reading = decrypted_string.split(', ')
                
                # Convert timestamp to datetime object
                timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
                day = timestamp.date()
                
                # Aggregate consumption by day
                if day not in daily_consumption:
                    daily_consumption[day] = 0.0
                daily_consumption[day] += float(reading)
        
        return daily_consumption

    def generate_consumption_graph(self):
        daily_consumption = self.calculate_neighborhood_daily_consumption()
        
        # Sorting the days to ensure the graph is in chronological order
        days = sorted(daily_consumption.keys())
        consumptions = [daily_consumption[day] for day in days]
        
        # Formatting days for the x-axis
        day_labels = [day.strftime('%Y-%m-%d') for day in days]
        
        # Generating the bar graph
        plt.figure(figsize=(10, 6))
        plt.bar(day_labels, consumptions, color='skyblue')
        
        plt.title('Neighborhood Daily Electricity Consumption')
        plt.xlabel('Day')
        plt.ylabel('Total Consumption (kW)')
        plt.xticks(rotation=45)
        plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels
        
        plt.show()