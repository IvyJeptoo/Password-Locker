import unittest
from credentials import Credentials, User


class TestUser(unittest.TestCase):
    '''
     Test class that defines test cases for the contact class behaviours.
     
     Args:
         unittest.TestCse: TestCase class that helps in creating test cases
    '''
    
    def setUp(self):
        '''
          Set up method to run before each test cases.
        '''
        
        self.new_user = User("Stacy "," Stacy2009") #Creates new user
        
    def test_init(self):
        '''
        tests if the object has been initialized properly
        '''
        
        self.assertEqual(self.new_user.username,"Stacy")
        self.assertEqual(self.new_user.password,"Stacy2009")
        
    def test_save_user(self):
        '''
        test case to test if the user object is being saved to the userlist
        '''
        #saving new user
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
            
            
    def tearDown(self):
           '''
           Cleans up after each test running
           '''
           User.user_list = []
           

class TestCredentials(unittest.TestCase):
    '''
    Test case defining test cases credentials class behaviour
    
    Args:
       unittest.TestCase: creates test cases
    '''
    
    def setUp(self):
        '''
        set up method to run before each test case
        '''
        
        #create credential object
        self.new_credentials = Credentials("twitter","Stacy","Stacy2009")
        
    def test_init(self):
        '''
        tests if object is initialized properly
        '''
        self.assertEqual(self.new_credentials.sitename,"twitter")
        self.assertEqual(self.new_credentials.accountname,"Stacy")
        self.assertEqual(self.new_credentials.login,"Stacy2009")
        
    def test_save_credentials(self):
        '''
        tests if the credential object is saved to the credential list
        '''
        
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def tearDown(self):
        '''
        cleans up after each test has run
        '''
        Credentials.credentials_list = []
        
    def test_save_multiple_credentials(self):
        '''
        tests if we can save multiple credential objects to credentials list
        '''
        
        self.new_credentials.save_credentials()
        #new credentials
        test_credentials1 = Credentials("instagram", "Stacy", "Stacy2009")
        test_credentials2 = Credentials("facebook", "Stacy", "Stacy2009")

        test_credentials1.save_credentials()
        test_credentials2.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),3)
        
    def test_search_credentials(self):
        '''
        finding credentials by name and displaying info
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("facebook","Stacy","Stacy2009")
        test_credentials.save_credentials()
        
        found_credential = Credentials.search_credentials("facebook")
        self.assertEqual(test_credentials.password,found_credential.password)
        
    def test_delete_credentials(self):
        '''
        tests if we can delete credentials
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Snapchat","Stacy2009")
        test_credentials.save_credentials()
        
        #deleting credentials
        self.new_credentials.delete_credentials(self)
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def test_update_credentials(self):
        '''
        unittest to test if a credential has been updated successfully
        '''
        self.new_cred.save_credentials()
        self.new_cred.password = "Stacy2009"
        self.new_cred.accountname = "Stacy"
        self.new_cred.save_credentials()
        self.assertEqual(self.new_credentials.password,"Stacy2009")
        self.assertEqual(self.new_credentials.username,"Stacy")
        self.assertEqual(self.new_credentials.sitename,"twitter")
        
if __name__ == '__main__':
    unittest.main()
        
    
    
        
    
        
        
        
        