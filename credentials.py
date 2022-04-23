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
    
    def newCredentials(self):
        print("My credentials are" + self.accountname + self.login) 
        
    def save_credentials(self):
        '''
        method that saves credentials objects into credentials list
        '''
        
        Credentials.credentials_list.append(self)
        
        
    @classmethod
    def find_by_name(cls,name):
        '''
        the method takes in accountname and it returns credential that matches the name
        
        Args:
          name: Account name to be searched for
          
        Returns:
          name of account that matches the name credential.
          
        '''
        for credentials in cls.credentials_list:
            if credentials.accountname == name:
                return credentials
            
    def delete_credentials(self):
        '''
        deletes user object from user list
        '''
        
        Credentials.credentials_list.remove(self)
        
    @classmethod
    def display_credentials(cls):
        '''
        returns credentials list
        '''
        return cls.credentials_list