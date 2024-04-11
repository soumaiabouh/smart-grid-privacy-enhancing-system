import os

# Import your modules here...
from smart_meter import *
from privacy_enhancing_system import *
from data_concentrator import *
from mdms_manager import *

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def print_menu():
    term_width = os.get_terminal_size().columns  # Get the current terminal width
    title = "Smart Meter Data Management System"
    print("=" * term_width)
    print(title.center(term_width))  # Center the title within the terminal width
    print("=" * term_width)
    print("[1] Run Neighborhood Statistics")
    print("[2] Run Billing Calculations")
    print("[3] Exit")
    print("=" * term_width)


def run_neighborhood_stats(mdms: MdmsManager, data_concentrator: DataConcentrator):
    filename1 = "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo2\\apart1.xlsx" #4320 rows ~ 3days 
    filename2 = "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo2\\apart2.xlsx"
    filename3 = "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo2\\apart3.xlsx"
    filename4 = "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo2\\apart4.xlsx"
    filename5 = "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo2\\apart5.xlsx"
    filename6 = "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo2\\apart6.xlsx"
    filename7 = "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo2\\apart7.xlsx"
    filename8 = "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo2\\apart8.xlsx"
    filename9 = "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo2\\apart9.xlsx"
    filename10 = "C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo2\\apart10.xlsx"
    
    sm1 = SmartMeter(pes_public_key, filename1, 4)
    sm2 = SmartMeter(pes_public_key, filename2, 4)
    sm3 = SmartMeter(pes_public_key, filename3, 4)
    sm4 = SmartMeter(pes_public_key, filename4, 4)
    sm5 = SmartMeter(pes_public_key, filename5, 4)
    sm6 = SmartMeter(pes_public_key, filename6, 4)
    sm7 = SmartMeter(pes_public_key, filename7, 4)
    sm8 = SmartMeter(pes_public_key, filename8, 4)
    sm9 = SmartMeter(pes_public_key, filename9, 4)
    sm10 = SmartMeter(pes_public_key, filename10, 4)
    
    data_concentrator.add_smart_meters([sm1, sm2, sm3, sm4, sm5, sm6, sm7, sm8, sm9, sm10])
    
    print("\nProcessing first batch of data...")
    data_concentrator.get_aggregated_data()
    data_concentrator.send_encrypted_data_to_mdms()
    
    print("\nProcessing second batch of data...")
    sm1.generate_data(filename1, 4)
    sm2.generate_data(filename2, 4)
    sm3.generate_data(filename3, 4)
    sm4.generate_data(filename4, 4)
    sm5.generate_data(filename5, 4)
    sm6.generate_data(filename6, 4)
    sm7.generate_data(filename7, 4)
    sm8.generate_data(filename8, 4)
    sm9.generate_data(filename9, 4)
    sm10.generate_data(filename10, 4)
    data_concentrator.get_aggregated_data()
    data_concentrator.send_encrypted_data_to_mdms()
    
    print("\nProcessing third batch of data...")
    sm1.generate_data(filename1, 4)
    sm2.generate_data(filename2, 4)
    sm3.generate_data(filename3, 4)
    sm4.generate_data(filename4, 4)
    sm5.generate_data(filename5, 4)
    sm6.generate_data(filename6, 4)
    sm7.generate_data(filename7, 4)
    sm8.generate_data(filename8, 4)
    sm9.generate_data(filename9, 4)
    sm10.generate_data(filename10, 4)
    data_concentrator.get_aggregated_data()
    data_concentrator.send_encrypted_data_to_mdms()
    
    #print(mdms.calculate_smart_meter_total_energy_consumption(sm1.get_id()))
    #print(mdms.calculate_smart_meter_total_energy_consumption(sm2.get_id()))
    print("\nSending the data to the database...")
    
    print("\nRunning analytics...")
    mdms.generate_consumption_graph() 
    
def run_billing_calculations(mdms: MdmsManager, data_concentrator: DataConcentrator):
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
    
    data_concentrator.send_encrypted_data_to_mdms()
     
    # TODO: Calculate bill for all users

   
if __name__ == "__main__":
    # Instantiate PES first to generate the key
    mdms = MdmsManager(1024)
    mdms_key = mdms.get_public_key()
    mdms.delete_all_records()

    pes = PES(mdms_key, 1024, 16)
    pes_public_key = pes.get_public_key()

    data_concentrator = DataConcentrator(pes, mdms)

    while True:
        clear_screen()
        print_menu()
        choice = input("Please enter your choice: ")

        if choice == '1':
            run_neighborhood_stats(mdms=mdms, data_concentrator=data_concentrator)
        elif choice == '2':
            run_billing_calculations(mdms=mdms, data_concentrator=data_concentrator)
        elif choice == '3':
            print("\nExiting program...")
            break
        else:
            print("Invalid choice, please try again.")
        input("Press Enter to continue...")  # Wait for user input to continue