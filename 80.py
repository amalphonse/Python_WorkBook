# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 20:08:36 2017

@author: anju

Create a script that lets the user submit a password until
they have satisfied three conditions:
    1) Password contains at least one number
    2) Contains one uppercase letter
    3) It is atleast 5 characters long
    4) GIve the exact reason why the password failed.
"""

while True:
    passwd_notes = []
    passwd = input("Enter password: ")
    if not any(i.isdigit() for i in passwd):
        passwd_notes.append("Atleast one digit is required.")
    if not any(i.isupper() for i in passwd):
        passwd_notes.append("Atleast one upper case required. ")
    if not len(passwd) >=5:
        passwd_notes.append("The length of password should 5 or greater.")
    if len(passwd_notes) == 0:
        print("Password good.")
        break
    else:
        print("Please check the following: ")
        for note in passwd_notes:
            print(note)