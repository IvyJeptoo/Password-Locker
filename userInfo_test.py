import unittest #imports unittest module
from userInfo import User #imports user class

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