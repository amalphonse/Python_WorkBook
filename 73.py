# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 19:50:38 2017

@author: anju
"""

"""
Multiply the values of the text in the URL file by 2 
and export the value to new txt file
"""

import pandas

data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")

data_2 = data * 2

data_2.to_csv("sample.txt",index=None)