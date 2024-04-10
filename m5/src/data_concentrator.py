from smart_meter import *
from privacy_enhancing_system import *

class DataConcentrator:
    def __init__(self, pes: PES):
        self.smList = []  # Initialize an empty list of smart meters
        self.pes = pes  # Privacy enhancing system instance
        self.aggregated_data_dict = {}  # Dictionary to store aggregated data
        self.last_processed_indices = {} # Maps smart meter IDs to last processed indices to avoid reaggregating everything

    def add_smart_meter(self, sm: SmartMeter):
        self.smList.append(sm)

    def add_smart_meters(self, smList):
        for sm in smList:
            self.smList.append(sm)
        
    def get_aggregated_data(self):
        for sm in self.smList:
            self._aggregate_data_for_sm(sm)
            
        #DEBUG
        # print("DATA CONCENTRATOR:")
        # print(self.aggregated_data_dict)
        # print(self.last_processed_indices)
            
    def _aggregate_data_for_sm(self, sm: SmartMeter):
        id = sm.get_id()
        encrypted_data = sm.get_encrypted_data()
        
        last_index = self.last_processed_indices.get(id, 0) 
        aggregated_data = self.pes.aggregate_and_encrypt(sm.get_encrypted_aes_key(), encrypted_data, start_index=last_index)
        
        if aggregated_data:
            new_last_index = last_index + len(encrypted_data[last_index:])
            self.last_processed_indices[id] = new_last_index
        
            if sm.get_id() not in self.aggregated_data_dict:
                self.aggregated_data_dict[id] = []
            self.aggregated_data_dict[id].append(aggregated_data)


    # TODO: Implement send_to_database_manager (send aggregated data dict)

