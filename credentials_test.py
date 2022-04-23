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
        
        
        
        