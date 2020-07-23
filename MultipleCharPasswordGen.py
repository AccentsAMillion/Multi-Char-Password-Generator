# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 06:43:39 2020
@author: Chris
"""

import random
import string


def generate_random_password(length):
    passwordChar = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    
    password = ''.join(random.choice(passwordChar) for i in range(length))
    
    print("Random Password is: " + password)
    
generate_random_password(15)