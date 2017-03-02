# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:34:58 2017

@author: anju
"""
import datetime as dt

user_age = int(input("Enter your age: "))

user_birth_year = dt.datetime.now().year - user_age
print("You were born back in %s." %(str(user_birth_year)))