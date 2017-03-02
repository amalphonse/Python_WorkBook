# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 23:19:08 2017

@author: anju
"""

"""
Question: Please create an empty file (manually as you normally create Python files) and name it requests.py . Make sure the file has that name exactly.

Then just paste the following code in the file (manually):

import requests
 
r = requests.get("http://www.pythonhow.com")
print(r.text[:100])
Executing the script will throw an error. Please fix that error so that you get the expected output and explain why the error happened.
"""

import requests
 
r = requests.get("http://www.pythonhow.com")
print(r.text[:100])