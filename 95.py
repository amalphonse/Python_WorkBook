# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 13:37:35 2017

@author: Anju
"""

#Comma Seperated Input

user_input = input("Enter your input: ")
user_input = user_input.split(",")

with open("sample_data.txt","a+") as f:
    for input_data in user_input:
        f.write(input_data + "\n")
