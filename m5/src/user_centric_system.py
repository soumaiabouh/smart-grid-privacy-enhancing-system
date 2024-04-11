from smart_meter import *
from privacy_enhancing_system import *
from mdms_manager import *
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
import getpass
import plotly.graph_objects as go
import os
from hashlib import pbkdf2_hmac

class UserCentricSystem:
    def __init__(self, sm: SmartMeter):
        self.sm = sm
        self.username = None
        self.encrypted_aes_key = None
        self.salt = None
        self.hashed_password = None
        self.rsa_key_pair = None

    def display(self):
        data_list = self.sm.get_encrypted_data()
        cipher_rsa = PKCS1_OAEP.new(self.rsa_key_pair)
        aes_key = cipher_rsa.decrypt(self.encrypted_aes_key)
        timestamps = []
        power = []
        for data in data_list:
            decrypted_data = self.decrypt(data, aes_key)
            timestamps.append(data['timestamp'])
            power.append(float(decrypted_data))
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=timestamps, y=power, mode='lines', name='Power [kW]'))
        fig.update_layout(title='Electricity Consumption', xaxis_title='Time', yaxis_title='Power [kW]')
        fig.show()

    def decrypt(self, data, aes_key):
        cipher_aes = AES.new(aes_key, AES.MODE_GCM, nonce=data['nonce'])
        return cipher_aes.decrypt_and_verify(data['encrypted_data'], data['tag'])

    def setCredentials(self, username: str, password: str):
        self.username = username
        self.salt = get_random_bytes(16)
        self.hashed_password = self.derive_key(password, self.salt)
        self.rsa_key_pair = RSA.generate(2048)
        self.encrypted_aes_key = self.sm._encrypt_key(self.get_public())

    def get_public(self):
        return self.rsa_key_pair.publickey()

    def authenticate(self, username, password):
        if username == self.username and self.derive_key(password, self.salt) == self.hashed_password:
            return True
        return False

    def prompt_credentials(self, new_user=False):
        username = input("Enter a username: ")
        password = getpass.getpass("Enter a password: ")
        if new_user:
            self.setCredentials(username, password)
            return 'SETUP_COMPLETE'
        elif not self.authenticate(username, password):
            print("Incorrect username or password.")
            return 'AUTH_FAILED'
        return 'AUTH_SUCCESSFUL'

    def user_dashboard(self):
        print_header("User Dashboard")
        while True:
            display_option = input("Display data? (YES/NO), Logout (LOGOUT), or Exit (EXIT): ").upper()
            if display_option == "YES":
                self.display()
            elif display_option == "LOGOUT":
                return 'LOGOUT'
            elif display_option == "EXIT":
                return 'EXIT'
            elif display_option == "NO":
                print("\tMore options to come!")
                continue
            else:
                print("Invalid option. Please choose YES, NO, LOGOUT, or EXIT.")

    def login(self):
        while True:
            print_header("Login to Smart Meter Data Management")
            if self.username is None:
                result = self.prompt_credentials(new_user=True)
                if result == 'SETUP_COMPLETE':
                    print("\nAccount successfully set up.")
                    input("\nPress Enter to continue...")
                elif result == 'AUTH_FAILED':
                    input("\nPress Enter to try again...")
                    continue
            else:
                result = self.prompt_credentials()
                if result == 'AUTH_FAILED':
                    input("\nPress Enter to try again...")
                    continue
            action = self.user_dashboard()
            if action == 'LOGOUT':
                continue
            elif action == 'EXIT':
                print("\nExiting the program...")
                break

    def derive_key(self, password: str, salt: bytes, key_length=32):
        derived = pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=key_length)
        return derived

def clear_console():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def print_header(title):
    clear_console()
    term_width = os.get_terminal_size().columns
    print(f"{'=' * term_width}")
    print(f"{title.center(term_width)}")
    print(f"{'=' *term_width}")

if __name__ == "__main__":
    mdms = MdmsManager(1024)
    mdms_key = mdms.get_public_key()
    pes = PES(mdms_key, 1024, 16)
    pes_public_key = pes.get_public_key()

    filename = "data\\demo\\apart1.xlsx"
    sm = SmartMeter(pes_public_key, filename, 1440)
    user = UserCentricSystem(sm)
    user.login()
