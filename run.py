import pyperclip, random, string
from credentials import Credentials
from userInfo import User

def create_user(username, password):
    '''
    creates a new user
    '''
    new_user = User(username, password)
    return new_user


def generate_login():
    '''
    function that generate a login
    '''
    phrase = string.digits + string.ascii_lowercase + string.ascii_uppercase
    while True:
        try:
            length = int(input("Enter desired length of login "))
            login = random.sample(phrase,length)
            
        except ValueError:
            print("Enter a valid number please!")
            continue
        else:
            login = ("".join(login))
            return login
        
def create_credentials(accountname, login):
    '''
    function to create new credential
    '''
    new_credentials = Credentials(accountname, login)
    return new_credentials
       

def save_credentials(credentials):
    '''
    function to save credentials
    '''   
    credentials.save_credentials()
    
def delete_credentials(credentials):
    '''
    function to delete credentials
    '''
    credentials.delete_credentials()
    
def find_credentials(names):
    '''
    function to find credentials by account name
    '''
    return Credentials.find_by_name(names)

def display_credentials():
    '''
    functions that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def main():
    print("Hello There, Welcome to Password Locker...")
    print("Please find navigation around the locker below")
    print("\n")
    print("lg => to login to your account")
    print("sn => to Sign-Up and create account.")
    short_code = input().lower()
    print("\n")
    if short_code == "sn":
                        print("Enter UserName")
                        username = input()
                        
                        print("Enter Password")
                        password = input()
                        
                        print("Confirm Password")
                        confirm_password = input()
                        
                        while confirm_password != password:
                            print("Try again! passwords does not match!")
                            print("Enter password")
                            password = input()
                            print("Confirm Password")
                            confirm_password = input()
                            
                        else:
                            print(f"Hi {username}, Your account has been successfully created!")
                            print("\n")
                            print("Login to your account")
                            print("Enter your Username")
                            username_input = input()
                            print("Entre your Password")
                            password_input = input()
                            
                        while username_input != username or password_input != password:
                            print("Invalid username or password")
                            
                            print("Enter your Username")
                            username_input = input()
                            print("Enter your Password")
                            password_input = input()
                            
                        else:
                            print(f"Hi {username}, Welcome to Password LOcker")
                            while True:
                              print("Choose an option to continue")
                              print("nc => to create new credentials")
                              print("dc => to display credentials")
                              print("cc => to copy credentials to clipboard")
                              print("da => to delete account credentias")
                              print("ex => to exit password locker")
                              
                              short_code = input().lower()
                              print("\n")
                              
                            
        

        
        
    