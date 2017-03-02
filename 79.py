# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 15:41:48 2017

@author: anju
"""

"""
Create a script that lets the user submit a password until
they have satisfied three conditions:
    1) Password contains at least one number
    2) Contains one uppercase letter
    3) It is atleast 5 characters long
"""


while True:
    passwd = input("Enter password: ")
    if any(i.isdigit() for i in passwd) and any(i.isupper() 
    for i in passwd) and len(passwd) >= 5:
        print("Password Good")
        break
    else:
        print("Password not good")