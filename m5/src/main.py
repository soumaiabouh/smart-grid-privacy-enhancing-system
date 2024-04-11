import os
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
    filename1 = "data\\demo2\\apart1.xlsx" 
    filename2 = "data\\demo2\\apart2.xlsx"
    filename3 = "data\\demo2\\apart3.xlsx"
    filename4 = "data\\demo2\\apart4.xlsx"
    filename5 = "data\\demo2\\apart5.xlsx"
    filename6 = "data\\demo2\\apart6.xlsx"
    filename7 = "data\\demo2\\apart7.xlsx"
    filename8 = "data\\demo2\\apart8.xlsx"
    filename9 = "data\\demo2\\apart9.xlsx"
    filename10 = "data\\demo2\\apart10.xlsx"
    
    # Init smart meters
    sm1 = SmartMeter(pes_public_key, filename1)
    sm2 = SmartMeter(pes_public_key, filename2)
    sm3 = SmartMeter(pes_public_key, filename3)
    sm4 = SmartMeter(pes_public_key, filename4)
    sm5 = SmartMeter(pes_public_key, filename5)
    sm6 = SmartMeter(pes_public_key, filename6)
    sm7 = SmartMeter(pes_public_key, filename7)
    sm8 = SmartMeter(pes_public_key, filename8)
    sm9 = SmartMeter(pes_public_key, filename9)
    sm10 = SmartMeter(pes_public_key, filename10)
    
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
    
    print("\nSending the data to the database...")
    data_concentrator.send_encrypted_data_to_mdms()
    
    input("\nPress Enter to continue...")  # Wait for user input to continue
    
    print("\nRunning analytics...")
    mdms.generate_consumption_graph() 
    
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
        input("\nPress Enter to continue...")  # Wait for user input to continue