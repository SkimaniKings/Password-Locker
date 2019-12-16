
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

def login_user(user_name,password):
    '''
  function that checks whether a user exist and then login the user in.
    '''
    check_user_exist = Credentials.check_user_exist(user_name,password)
    
    return check_user_exist

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
        short_code=input()
        if short_code=='cu' :
            print("welcome. Follow this simple steps to Create an account")
            print('-'*50)
            print("First name ....")
            f_name=input()
            print('Last name....')
            l_name=input()
            print("Enter Phone Number")
            phone=input()
            print('Enter email address ....')
            email=input()
            
            # save_user(create_user(f_name,l_name,phone,email)) #save and create user
            print(f"Please confirn your details fname:{f_name} lname:{l_name}  phone:{phone} email:{email}")
            print("Enter 'y' to continue or 'n' to input new data")
            response=input()
            if response =='y':
                print(f"Hello {f_name} {l_name} . Your account has been successfuly created.")
            else:
                 print("Kindly use this short codes CU: To create new user account LG: To log in to existing account DA: To display list of accounts EX:To exit")
        elif short_code == 'lg':
            print("Welcome.What site would you love to create an account for?")
            site = input()
            print(f"Welcome to {site}. Have fun!")
            print('-'*50)
            print("First name ....")
            f_name=input()
            print('Last name....')
            l_name=input()
            print('Enter email address ....')
            email=input()
            
            
            
        else:
            print("You have made an invalid choice. Please try again")
            
if __name__ == '__main__':
    
    main()
    