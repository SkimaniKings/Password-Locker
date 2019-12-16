
from credentials import Credentials
import user 
def create_user(fname,lname,phone,email):
    '''
    Function to create a new user
    '''
    new_user = (fname,lname,phone,email)
    return new_user
def save_user(user):
    """
    Function to save user
    """
    user.save_user_details()
def create_credential(uname, pword, email):
    """
    Function to create new user credentials
    """
    new_credential = Credentials(uname, pword, email)
    return new_credential 

def save_credential(credential):
    """
    Function to save user credentials
    """
    credential.save_credential()

def delete_credentials(credential):
    """
    Function to delete all users credentials
    """
    credential.delete_credential()
def display_credential(Credentials):
    '''
    Function that displays credentials
    '''
    return Credentials.display_credential()
def display_user(user):
    """
    Function that returns saved users
    """
    return user.display_users()

def main():
    print("Hello! Welcome to Password-Locker")
    print("Choose action you would wish to take")
    print('\n')
    print('-'*100)
    while True:
        print("Kindly use this short codes CU: To create new user account LG: To log in to existing account DA: To display list of accounts EX:To exit")
        short_code=input().lower()
if __name__ == '__main__':
  main()
    