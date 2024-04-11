import pandas as pd

def aggregate_and_save_data(file_path, output_file_path):
    # Load the Excel file without headers
    data = pd.read_excel(file_path, header=None, skiprows=[0], names=['Timestamp', 'Value'])
        
    # Ensure 'Timestamp' is a datetime type
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    
    # Set 'Timestamp' as the index for resampling
    data.set_index('Timestamp', inplace=True)
    
    # Sum the data over 12-hour periods
    aggregated_data = data.resample('12H').sum()
    
    # Reset index so that 'Timestamp' is included as a column for saving
    aggregated_data_reset = aggregated_data.reset_index()
    
    # Save to Excel without headers
    aggregated_data_reset.to_excel(output_file_path, header=False, index=False)
    
    print(f"Aggregated data has been saved to {output_file_path}")

for i in range(1, 11):
    file_path = f'C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo\\apart{i}.xlsx'  # Replace with the path to your original Excel file
    output_file_path = f'C:\\Users\\soums\\Desktop\\University\\W2024\\COMP555\\Project\\c555w24-t7\\m5\\src\\data\\demo2\\apart{i}.xlsx'  # Output file with kW in the name for clarity
    aggregate_and_save_data(file_path, output_file_path)
