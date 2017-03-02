# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 08:59:29 2017

@author: anju
"""

"""
Question: Please add a new employee to the dictionary.

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}
Expected output: 

{'employees': [{'firstName': 'John', 'lastName': 'Doe'},
               {'firstName': 'Anna', 'lastName': 'Smith'},
               {'firstName': 'Peter', 'lastName': 'Jones'},
               {'firstName': 'Albert', 'lastName': 'Bert'}],
 'owners': [{'firstName': 'Jack', 'lastName': 'Petter'},
            {'firstName': 'Jessy', 'lastName': 'Petter'}]}
 """
 
d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

d['employees'] = [{"firstName":"Albert","lastName":"Bert"}]

print(d)

"""
runfile('C:/Users/alphy/Documents/Anju_Documents/Python_Learning/python_workbook/55.py', wdir='C:/Users/alphy/Documents/Anju_Documents/Python_Learning/python_workbook')
{'employees': [{'firstName': 'Albert', 'lastName': 'Bert'}], 'owners': [{'firstName': 'Jack', 'lastName': 'Petter'}, {'firstName': 'Jessy', 'lastName': 'Petter'}]}
"""