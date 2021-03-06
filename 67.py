# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 23:08:29 2017

@author: anju
"""
"""
Question: Create an English to Portuguese translation program.

The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source. In addition, try to return the message "We couldn't find that word!" when the user enters a word that is not in the dictionary.

d = dict(weather = "clima", earth = "terra", rain = "chuva") 
"""
"""
d = dict(weather = "clima", earth = "terra", rain = "chuva")

def vocabulary(word):
    if word in d:
        return(d[word])
    else:
        return "We couldn't find that word"
        
word = input("Enter word: ")
print(vocabulary(word))
"""

#Alternate solution

d = dict(weather = "clima", earth = "terra", rain = "chuva")

def vocabulary(word):
    try:
        return(d[word])
    except KeyError:
        return "We couldn't find that word"
        
word = input("Enter word: ")
print(vocabulary(word))