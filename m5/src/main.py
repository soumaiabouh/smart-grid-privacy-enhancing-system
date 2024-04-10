from smart_meter import *
from privacy_enhancing_system import *
from data_concentrator import *
from mdms_manager import *

if __name__=="__main__":
    # Instantiate PES first to generate the key
    mdms = MdmsManager(1024)
    mdms_key = mdms.get_public_key()
    mdms.delete_all_records()
    
    pes = PES(mdms_key, 1024, 16)
    pes_public_key = pes.get_public_key()
    
    data_concentrator = DataConcentrator(pes)
    
    # Setting up the filenames for the 10 sms
    filename1 = "data\\demo\\apart1.xlsx" #4320 rows ~ 3days 
    filename2 = "data\\demo\\apart2.xlsx"
    filename3 = "data\\demo\\apart3.xlsx"
    filename4 = "data\\demo\\apart4.xlsx"
    filename5 = "data\\demo\\apart5.xlsx"
    filename6 = "data\\demo\\apart6.xlsx"
    filename7 = "data\\demo\\apart7.xlsx"
    filename8 = "data\\demo\\apart8.xlsx"
    filename9 = "data\\demo\\apart9.xlsx"
    filename10 = "data\\demo\\apart10.xlsx"
    
    sm1 = SmartMeter(pes_public_key, filename1, 10)
    sm2 = SmartMeter(pes_public_key, filename2, 10)
    sm3 = SmartMeter(pes_public_key, filename3, 10)
    sm4 = SmartMeter(pes_public_key, filename4, 10)
    sm5 = SmartMeter(pes_public_key, filename5, 10)
    sm6 = SmartMeter(pes_public_key, filename6, 10)
    sm7 = SmartMeter(pes_public_key, filename7, 10)
    sm8 = SmartMeter(pes_public_key, filename8, 10)
    sm9 = SmartMeter(pes_public_key, filename9, 10)
    sm10 = SmartMeter(pes_public_key, filename10, 10)
    
    data_concentrator.add_smart_meters([sm1, sm2, sm3, sm4, sm5, sm6, sm7, sm8, sm9, sm10])
    data_concentrator.get_aggregated_data()
    
    aggregated_data_encrypted = data_concentrator.aggregated_data_dict
    mdms._decrypt_data(aggregated_data_encrypted)
    print(mdms.decrypted_data_dict)
    
    mdms.send_data_to_mdms(aggregated_data_encrypted)
    # mdms.print_all_data()
    
    print(mdms.calculate_smart_meter_total_energy_consumption(sm1.get_id()))
    print(mdms.calculate_smart_meter_total_energy_consumption(sm2.get_id()))
    