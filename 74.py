# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:02:38 2017

@author: anju
"""

import pandas

data_1 = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")

data_2 = pandas.read_csv("http://pythonhow.com/data/sampledata_x_2.txt")

data = pandas.concat([data_1,data_2])

data.to_csv("sample2.txt",index=None)