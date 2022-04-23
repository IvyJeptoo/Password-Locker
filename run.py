import pyperclip
from userInfo import User

def create_def(username, password):
    '''
    creates a new user
    '''
    new_user = User(username, password)
    return new_user