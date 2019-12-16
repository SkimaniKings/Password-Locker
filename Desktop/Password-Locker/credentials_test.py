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
if __name__ == '__main__':
    unittest.main()