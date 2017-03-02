# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 13:53:14 2017

@author: Anju
"""

#Advanced File Writer

f = open("user_data_1.txt","a+")

while True:
    input_data = input("Enter data:")
    if input_data == "SAVE":
        f.close()
        f = open("user_data_1.txt","a+")   
    elif input_data == 'CLOSE':
        f.close()
        break
    else:
        f.write(input_data+"\n")
        