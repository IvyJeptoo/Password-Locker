import unittest
from credentials import Credentials

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
        self.new_credentials = Credentials("Instagram","Stacy2009")
        
    def test_init(self):
        '''
        tests if object is initialized properly
        '''
        self.assertEqual(self.new_credentials.accountname,"Instagram")
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
        test_credentials = Credentials("New", "Key")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
        
    def test_find_credentials_by_name(self):
        '''
        finding credentials by name and displaying info
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Twitter","Stacy2009")
        test_credentials.save_credentials()
        
        found_credential = Credentials.find_by_name("Twitter")
        self.assertEqual(test_credentials.accountname,found_credential.accountname)
        
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
        
    def test_display_all_credentials(self):
        '''
        returns a list of all the credentials saved
        '''
        
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
        
        
if __name__ == '__main__':
    unittest.main()
        
    
    
        
    
        
        
        
        