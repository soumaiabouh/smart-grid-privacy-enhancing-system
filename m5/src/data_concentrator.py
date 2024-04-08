from smart_meter import *
from privacy_enhancing_system import *

class DataConcentrator:
    def __init__(self, pes: PES):
        self.smList = []  # Initialize an empty list of smart meters
        self.pes = pes  # Privacy enhancing system instance
        self.time = 0  # Initialize time
        self.aggregated_data_dict = {}  # Dictionary to store aggregated data

    def add_smart_meter(self, sm: SmartMeter):
        self.smList.append(sm)

    def get_aggregated_data(self, time_range = 60):
        for sm in self.smList:
            aggregated_data = self.pes.aggregate_and_encrypt(sm.get_encrypted_aes_key(), sm.get_encrypted_data())
            
            if sm.id not in self.aggregated_data_dict:
                self.aggregated_data_dict[sm.id] = []  # Initialize list for the smart meter if not present
            # Append encrypted data for the current time to the data dictionary
            self.aggregated_data_dict[sm.id].append(aggregated_data)


    # TODO: Implement send_to_database (send aggregated data dict)
