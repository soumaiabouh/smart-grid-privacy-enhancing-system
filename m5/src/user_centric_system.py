from smart_meter import SmartMeter
from Crypto.Cipher import AES
import plotly.graph_objects as go
from privacy import PES
from MDMS import * 
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes


class UserCentricSystem:
    def __init__(self, sm: SmartMeter):
        self.sm = sm
        self.username = None
        self.aes_key = sm.aes_key
        self.salt = None
        self.key = None
        
    def display(self):
        # decrypts sm data from AES
        data_list = self.sm.get_encrypted_data()

        # Decrypt each piece of reading and store it
        timestamps = []
        power = [] 

        for data in data_list:
            # Format of data: {timestamp, encrypted_data, tag, nonce}
            decrypted_data = self.decrypt(data)
            timestamps.append(data['timestamp'])
            power.append(float(decrypted_data))

        # time series graph
        fig = go.Figure() 
        fig.add_trace(go.Scatter(x=timestamps, y=power, mode='lines', name='Power [kW]'))
        fig.update_layout(title='Electricity Consumption', xaxis_title='Time', yaxis_title='Power [kW]')
        fig.show()

    def decrypt(self, data):
        # helper function that decrypts data
        cipher_aes = AES.new(self.aes_key, AES.MODE_GCM, nonce=data['nonce'])
        return cipher_aes.decrypt_and_verify(data['encrypted_data'], data['tag'])

    def setCredentials(self, username: str, password: str):
        # set username 
        self.username = username 
        # set salt 
        self.salt = get_random_bytes(16)
        # derive key from password
        self.key = self.derive_key(password,self.salt)
       
    def login(self):
        # "main" function
        # If the username is NULL (aka this is the user's first login), then we prompt them for their username and password and call setCredentials().
        # Ask user if they want to display data. If yes, prompt user to enter username and password to log in, then call display().
        # Wait for user to log out/end the program.

        if self.username is None:
            print("New User.")
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            self.setCredentials(username, password)
            print("Account successfully set up.")
        
        display_option = input("Display data? (YES/NO): ").upper()
        if display_option == "YES":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if username == self.username:  # Checking if username matches
                # Implement authentication logic with password
                if self.derive_key(password, self.salt) == self.key: 
                    self.display()
                else:
                    print("Incorrect password.")
            else:
                print("Invalid username.")
        elif display_option == "NO":
            pass
        else:
            print("Invalid option.")

    def derive_key(self, password: str, salt: bytes, key_length= 32):
        derived = PBKDF2(password, salt, dkLen=key_length)
        return derived
