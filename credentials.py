import pyperclip
from userInfo import User

class Credentials:
    '''
    creates an instance of user credentials
    '''
    
    credentials_list = []
    
    def __init__(self,accountname,login):
        '''
        define object properties
        
        Args:
        accountname: Account name
        login: Account password
        '''
        
        self.accountname = accountname
        self.login = login
        
    