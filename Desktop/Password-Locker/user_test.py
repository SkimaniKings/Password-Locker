import unittest 
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = User("Simon","Kimani", "0713813919","kimanisimon856@gmail.com")
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Simon")
        self.assertEqual(self.new_user.last_name,"Kimani")
        self.assertEqual(self.new_user.phone_number,"0713813919")
        self.assertEqual(self.new_user.email,"kimanisimon856@gmail.com")
    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved into
         the users array
        """
        self.new_user.save_user_details()  
        self.assertEqual(len(User.user_list), 1)

if __name__ == '__main__':
    unittest.main()
