from hashlib import new
import pyperclip
from credentials import Credentials
from userInfo import User

def create_user(username, password):
    '''
    creates a new user
    '''
    new_user = User(username, password)
    return new_user

def create_credentials(accountname, login):
    '''
    function to create new credential
    '''
    new_credentials = Credentials(accountname, login)
    return new_credentials