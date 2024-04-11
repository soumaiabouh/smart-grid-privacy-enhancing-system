from smart_meter import *
from privacy_enhancing_system import *
from mdms_manager import * 
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
import getpass
import plotly.graph_objects as go

class UserCentricSystem:
    def __init__(self, sm: SmartMeter):
        self.sm = sm
        self.username = None
        self.encrypted_aes_key = None
        self.salt = None
        self.key = None
        self.rsa_key_pair = None
        
    def display(self):
        # decrypts sm data from AES
        data_list = self.sm.get_encrypted_data()

        # decrypt aes key for session 
        # obtain encrypted key 
        cipher_rsa = PKCS1_OAEP.new(self.rsa_key_pair)  # Creates a new RSA cipher object for decryption
        aes_key = cipher_rsa.decrypt(self.encrypted_aes_key) 

        # Decrypt each piece of reading and store it temporarily
        timestamps = []
        power = [] 

        for data in data_list:
            # Format of data: {timestamp, encrypted_data, tag, nonce}
            decrypted_data = self.decrypt(data, aes_key)
            timestamps.append(data['timestamp'])
            power.append(float(decrypted_data))
        
        # time series graph
        fig = go.Figure() 
        fig.add_trace(go.Scatter(x=timestamps, y=power, mode='lines', name='Power [kW]'))
        fig.update_layout(title='Electricity Consumption', xaxis_title='Time', yaxis_title='Power [kW]')
        fig.show()

        timestamps.clear()
        power.clear()

    def decrypt(self, data, aes_key):
        # helper function that decrypts data
        cipher_aes = AES.new(aes_key, AES.MODE_GCM, nonce=data['nonce'])
        return cipher_aes.decrypt_and_verify(data['encrypted_data'], data['tag'])

    def setCredentials(self, username: str, password: str):
        # set username 
        self.username = username 
        # salt is randomly and uniquely generated for each user
        # A (byte) string to use for better protection from dictionary attacks. 
        # This value does not need to be kept secret, but it should be randomly chosen for each derivation. 
        self.salt = get_random_bytes(16)
        # derive key from password
        self.key = self.derive_key(password,self.salt)
        # generate key pair 
        self.rsa_key_pair = RSA.generate(2048)
        # obtain encrypted key 
        self.encrypted_aes_key = sm._encrypt_key(self.get_public())
    
    def get_public(self):
        # fucntion returning public key 
        return self.rsa_key_pair.publickey()
       
    def login(self):
        # "main" function
        # If the username is NULL (aka this is the user's first login), then we prompt them for their username and password and call setCredentials().
        # Ask user if they want to display data. If yes, prompt user to enter username and password to log in, then call display().
        # Wait for user to log out/end the program.

        if self.username is None:
            print("New User")
            username = input("Enter a username: ")
            password = getpass.getpass("Enter a password: ")
            self.setCredentials(username, password)
            print("Account successfully set up.")
        
        display_option = input("Display data? (YES/NO): ").upper()
        if display_option == "YES":
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")
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
        # iteration count determines the computational complexity cost of key derivation process
        derived = PBKDF2(password, salt, dkLen=key_length, count=100000) # password based key derivation function
        return derived
    
