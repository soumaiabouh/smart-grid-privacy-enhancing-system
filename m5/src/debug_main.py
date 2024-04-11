import os

# Import your modules here...
from smart_meter import *
from privacy_enhancing_system import *
from data_concentrator import *
from mdms_manager import *

def run_billing_calculations(mdms: MdmsManager, data_concentrator: DataConcentrator):
    # Setting up the filenames for the 10 sms
    filenames = ["C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo\\apart1.xlsx", 
                 "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo\\apart2.xlsx",
                 "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo\\apart3.xlsx",
                 "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo\\apart4.xlsx",
                 "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo\\apart5.xlsx",
                 "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo\\apart6.xlsx",
                 "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo\\apart7.xlsx",
                 "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo\\apart8.xlsx",
                 "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo\\apart9.xlsx",
                 "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo\\apart10.xlsx"]
    
    # Create SmartMeter instances and store them in a list
    smart_meters = [SmartMeter(pes_public_key, filename, 10) for filename in filenames]

    # Add smart meters to the data concentrator
    for sm in tqdm(smart_meters, desc="Generating data"):
        data_concentrator.add_smart_meters([sm])
        data_concentrator.get_aggregated_data(sm)
    
    data_concentrator.send_encrypted_data_to_mdms()

    # Now run the billing calculations for a chosen smart meter
    while True:
        try:
            index = int(input("Choose a smart meter between 1 and 10: ")) - 1  # Subtract 1 for zero-based index
            if 0 <= index < len(smart_meters):
                sm = smart_meters[index]
                sm_id = sm.get_id()
                consumption = mdms.calculate_smart_meter_total_energy_consumption(sm_id)
                price = consumption * 0.073  # Assuming consumption is in Wh
                
                print(f"\nSmart Meter ID: {index+1}")
                print(f"Total Energy Consumption: {consumption:.2f} kW")
                print(f"Total Bill Based on Current Energy Consumption: ${price:.2f}")
            else:
                print("Invalid input. Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

        again = input("\nWould you like to calculate the bill for another meter? (YES/NO): ").upper()
        if again != "YES":
            break
   
if __name__ == "__main__":
    # Instantiate PES first to generate the key
    mdms = MdmsManager(1024)
    mdms_key = mdms.get_public_key()
    mdms.delete_all_records()

    pes = PES(mdms_key, 1024, 16)
    pes_public_key = pes.get_public_key()

    data_concentrator = DataConcentrator(pes, mdms)

    run_billing_calculations(mdms=mdms, data_concentrator=data_concentrator)
    