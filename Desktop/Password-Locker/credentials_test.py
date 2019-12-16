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
if __name__ == '__main__':
    unittest.main()