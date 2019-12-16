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
    def save_credentials(self):
        '''
        test to confirm if the application saves multiple users
        '''
        Credentials.credentials_list.append(self)