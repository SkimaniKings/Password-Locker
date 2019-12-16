#!/usr/bin/env python3.6
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
    new_credential = Credential(uname, pword, email)
    return new_credential

def save_credential(credential):
    """
    Function to save user credentials
    """
    credential.save_credential()
    