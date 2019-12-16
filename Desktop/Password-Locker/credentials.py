class Credentials:
    '''
    A class that generates new instances for users
    '''
    credentials_list=[]
    def __init__(self,acc_name,acc_email,acc_password):
        self.acc_name=acc_name
        self.acc_email=acc_email
        self.acc_password=acc_password
    def save_credentials(self):
        '''
        save credentials list into credentials list array
        '''
        Credentials.credentials_list.append(self)
   
    def delete_account(self):
        '''
        method that allows application to delete accounts
        '''
        Credentials.credentials_list.remove(self)
    @classmethod
    def display_credentials(cls):
        """
        method that returns the class array
        """
        return cls.credentials_list
    @classmethod
    def check_user_exist(cls,user_name,password):
        
    
    #Method that checks if a user exist from user list.
        for user in User.user_list:
            if user.user_name == user_name and user.password == password:
                return True
            return False