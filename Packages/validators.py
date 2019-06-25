#Function to validate a phone number

import re

def phonenumbervalidator(number):
    pattern = '^[6-9]{1}[0-9]{9}$|^[0][6-9]{1}[0-9]{9}$'
    if re.match(pattern,(number)):
        return True
    else:
        return False 
    
    
import re

def emailvalidator(email):
    pattern = '^[0-9a-z][0-9a-z_.]{4,13}[0-9a-z][@][a-z0-9]{4,15}[.][a-z]{2,5}$'
    if re.match(pattern,email):
        return True
    else:
        return False 