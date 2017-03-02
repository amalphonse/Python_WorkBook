# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 09:20:00 2017

@author: anju
"""


"""

Question: Please download the file in the attachment and 
use Python
 to print out its content.

"""
from pprint import pprint
import json

with open("company2.json","r") as f:
    d = json.loads(f.read())
    

pprint(d)