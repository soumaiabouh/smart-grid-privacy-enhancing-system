class DataConcentrator:
    def __init__(self, PES):
        self.smList = []  # Initialize an empty list of smart meters
        self.pes = PES  # Privacy enhancing system instance
        self.data_dict = {}  # Dictionary to store data from each smart meter
        self.time = 0  # Initialize time
        self.aggregated_data_dict = {}  # Dictionary to store aggregated data

    def add_smart_meter(self, sm):
        self.smList.append(sm)

    def get_aggregated_data(self):
        minutes = 10  # Number of minutes to aggregate data, hard-coded for nowZ
        while self.time < minutes:
            for sm in self.smList:
                # Assuming sm.get_encrypted_data() returns encrypted data for a specific time
                encrypted_data = sm.get_encrypted_data(self.time)
                if sm.id not in self.data_dict:
                    self.data_dict[sm.id] = []  # Initialize list for the smart meter if not present
                # Append encrypted data for the current time to the data dictionary
                self.data_dict[sm.id].append(encrypted_data)
            self.time += 1

        # Aggregate data for each smart meter and store in aggregated_data_dict
        for sm_id, encrypted_data_list in self.data_dict.items():
            aggregated_data = self.pes.pallierEncrypt(decryption_keyAES, encrypted_data_list)
            self.aggregated_data_dict[sm_id] = aggregated_data

        # Clear data_dict for the next aggregation
        self.data_dict.clear()

    # TODO: Implement send_to_database (send aggregated data dict)
