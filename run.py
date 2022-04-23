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
        

        
        
    