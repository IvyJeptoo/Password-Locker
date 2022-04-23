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
           
if __name__ == '__main__':
    unittest.main()
        