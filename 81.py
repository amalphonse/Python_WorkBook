# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 11:03:12 2017

@author: anju
"""
#Checking if username exists
while True:
    user_name = input("Enter user name: ")
    with open("users.txt","r") as f:
        users = f.readlines()
        users = [i.strip("\n") for i in users]
        if user_name in users:
            print("username exists")
            continue
        else:
            print("username good.")
            break


#password check

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