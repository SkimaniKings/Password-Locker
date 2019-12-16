
import credentials
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
def main():
    print("Hello! Welcome to Password-Locker")
    print("Choose action you would wish to take")
if __name__ == '__main__':
    
    main()
    