import os

# Import your modules here...
from smart_meter import *
from privacy_enhancing_system import *
from data_concentrator import *
from mdms_manager import *

def run_neighborhood_stats(mdms: MdmsManager, data_concentrator: DataConcentrator):
    filename1 = "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo2\\apart1.xlsx"
    filename2 = "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo2\\apart2.xlsx"
    filename3 = "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo2\\apart3.xlsx"
    filename4 = "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo2\\apart4.xlsx"
    filename5 = "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo2\\apart5.xlsx"
    filename6 = "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo2\\apart6.xlsx"
    filename7 = "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo2\\apart7.xlsx"
    filename8 = "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo2\\apart8.xlsx"
    filename9 = "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo2\\apart9.xlsx"
    filename10 = "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo2\\apart10.xlsx"
 
    # Init smart meters
    sm1 = SmartMeter(pes_public_key, filename1, 0)
    sm2 = SmartMeter(pes_public_key, filename2, 0)
    sm3 = SmartMeter(pes_public_key, filename3, 0)
    sm4 = SmartMeter(pes_public_key, filename4, 0)
    sm5 = SmartMeter(pes_public_key, filename5, 0)
    sm6 = SmartMeter(pes_public_key, filename6, 0)
    sm7 = SmartMeter(pes_public_key, filename7, 0)
    sm8 = SmartMeter(pes_public_key, filename8, 0)
    sm9 = SmartMeter(pes_public_key, filename9, 0)
    sm10 = SmartMeter(pes_public_key, filename10, 0)
    
    data_concentrator.add_smart_meters([sm1, sm2, sm3, sm4, sm5, sm6, sm7, sm8, sm9, sm10])
    
    for i in tqdm(range(1, 8), desc="Generating the data"):
        sm1.generate_data(filename1, 2)
        sm2.generate_data(filename2, 2)
        sm3.generate_data(filename3, 2)
        sm4.generate_data(filename4, 2)
        sm5.generate_data(filename5, 2)
        sm6.generate_data(filename6, 2)
        sm7.generate_data(filename7, 2)
        sm8.generate_data(filename8, 2)
        sm9.generate_data(filename9, 2)
        sm10.generate_data(filename10, 2)
        data_concentrator.get_aggregated_data()
    
    data_concentrator.send_encrypted_data_to_mdms()
        
    print("\nSending the data to the database...")
    
    print("\nRunning analytics...")
    mdms.generate_consumption_graph() 
   
if __name__ == "__main__":
    # Instantiate PES first to generate the key
    mdms = MdmsManager(1024)
    mdms_key = mdms.get_public_key()
    mdms.delete_all_records()

    pes = PES(mdms_key, 1024, 16)
    pes_public_key = pes.get_public_key()

    data_concentrator = DataConcentrator(pes, mdms)

    run_neighborhood_stats(mdms=mdms, data_concentrator=data_concentrator)
    