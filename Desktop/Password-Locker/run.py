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
