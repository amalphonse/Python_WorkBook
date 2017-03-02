# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 22:08:32 2017

@author: anju
"""

"""
Question: Create an English to Portuguese translation program.

The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source.

d = dict(weather = "clima", earth = "terra", rain = "chuva") 
"""


d = dict(weather = "clima", earth = "terra", rain = "chuva")

word = input("Enter word: ")

if word in d:
    print(d[word])