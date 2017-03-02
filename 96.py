# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 13:47:30 2017

@author: Anju
"""

#File Writer

"""
Create a program that asks user to submit text repeatedly
until CLOSE is input
"""

f = open("user_data.txt","a+")

while True:
    input_data = input("Enter data:")
    if input_data == 'CLOSE':
        f.close()
        break
    else:
        f.write(input_data+"\n")