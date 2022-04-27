from random import randint



class User:
    '''
    This class creates an instance of a user
    '''
    user_list = []
    
    def __init__(self, username,password):
        '''
        defines property for the object
        
        Args:
            Username: user's name
            Password: user's account password
        '''
        
        self.username = username
        self.password = password
        
    def newUser(self):
        print("My user details" + self.username + self.password)
        
        
    def save_user(self):
        '''
        saves user objects in the user_list
        '''
        
        User.user_list.append(self)
        
    

class Credentials:
    '''
    creates an instance of user credentials
    '''
    
    credentials_list = []
    
    def __init__(self,accountname,sitename,login):
        '''
        define object properties
        
        Args:
        accountname: Account name
        login: Account password
        
        '''
        
        self.accountname = accountname
        self.sitename = sitename
        self.login = login
    

    
    def delete_credentials(self):
        '''
        deletes user object from user list
        '''
        
        Credentials.credentials_list.remove(self)   
    def save_credentials(self):
        '''
        method that saves credentials objects into credentials list
        '''
        
        Credentials.credentials_list.append(self)
    
    def generate_password(ln):
        '''
        generate random password method
        '''
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890=?!#/@~$*"
        password = " "
        for i in range(ln):
            password += chars[randint(0, len(chars) - 1)]
        return password   
        
    @classmethod
    def search_credentials(cls,sitename):
        '''
        the method takes in accountname and it returns credential that matches the name
        
        Args:
          name: Account name to be searched for
          
        Returns:
          name of account that matches the name credential.
          
        '''
        for credentials in cls.credentials_list:
            if credentials.accountname == sitename:
                return credentials
    def aunthenticate(cls,username,password):
        '''
        method to check if user exists in users
        '''  
        active_user = ""
        for user in User.users:
            if (user.username == username and user.password == password):
                active_user = user.username
                
        return active_user        
   
        
    @classmethod
    def display_credentials(cls):
        '''
        returns credentials list
        '''
        return cls.credentials_list