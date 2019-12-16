import unittest
from credentials import Credentials
class TestUser(unittest.TestCase):
    
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_credentials_list=Credentials("twitter","kimsimo10@gmail.com","password")
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials_list.acc_name,"twitter")
        self.assertEqual(self.new_credentials_list.acc_email,"kimsimo10@gmail.com")
        self.assertEqual(self.new_credentials_list.acc_password,"password")
    def test_save_credentials(self):
        '''
        test to test if the credentials are being saved
        '''
        self.new_credentials_list.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
    def test_save_multiple_credentials(self):
        '''
        test to confirm if the application saves multiple users
        '''
        self.new_credentials_list.save_credentials()
        test_credentials=("facebook","testerT@gmail.com","password")
        # test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
    def test_display_credentials(self):
        '''
        A test to check if saved credentials can be displayed
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)  
        
if __name__ == '__main__':
    unittest.main()