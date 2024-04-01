class DataConcentrator:
    def __init__(self, PES):
        self.smList = []  # Init an empty list
        self.pes = PES  # Privacy enhancing system instance
        self.data_dict = {} # { sm1: {data}, sm2: {data}, sm3: {data}, ...}

    def add_smart_meter(self, sm):
        self.smList.append(sm)

    def get_aggregated_data(self):
        count = 0
        for sm in self.smList:
            self.pes.pallierEncrypt()  # Assuming pallierEncrypt is a method of PES
