from smart_meter import *
from privacy_enhancing_system import *
from data_concentrator import *

if __name__=="__main__":
    # Instantiate PES first to generate the key
    pes = PES(1024)
    pes_public_key = pes.get_public_key()
    
    filename1 = "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo\\apart1.xlsx"
    
    sm1 = SmartMeter(pes_public_key, filename1)
    data = pes.aggregate_and_encrypt(sm1.get_encrypted_aes_key(), sm1.get_encrypted_data())
    print(data)                 
    print(len(sm1.encrypted_data_list))
    
    sm1.generate_data(filename1, 10)
    data2 = pes.aggregate_and_encrypt(sm1.get_encrypted_aes_key(), sm1.get_encrypted_data(), start_index=60)
    print(data2)
    print(len(sm1.encrypted_data_list))
    
    # print(data)
    # Now we have the data. Need to send that to the MDMS, where it could possibly be decrypted. 