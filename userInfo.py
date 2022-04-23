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