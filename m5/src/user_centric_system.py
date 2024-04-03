from smart_meter import SmartMeter

class UserCentricSystem:
    def __init__(self, sm: SmartMeter):
        self.sm = sm
        self.encryption_key = None
        self.username = None
        
    def display(self):
        # decrypts sm data from AES
        # graph
        # do not keep this data
        pass
        
    def setCredentials(self, username: str, password: str):
        # get SmartMeter's key
        # encrypt it using the user's credentials
        # store encrypted key in this object (self/class)
        pass
    
    def login(self):
        # "main" function
        # If the username is NULL (aka this is the user's first login), then we prompt them for their username and password and call setCredentials().
        # Ask user if they want to display data. If yes, prompt user to enter username and password to log in, then call display().
        # Wait for user to log out/end the program.


        # Rough example:
        if self.username is None:
            self.username = input("Enter your username: ")
            password = input("Enter your password: ")
            self.setCredentials(self.username, password)
        
        display_option = input("Display data? (YES/NO): ").upper()
        if display_option == "YES":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if username == self.username:  # Checking if username matches
                # Implement authentication logic with password
                self.display()
            else:
                print("Invalid username.")
        elif display_option == "NO":
            # Do something else
            pass
        else:
            print("Invalid option.")
