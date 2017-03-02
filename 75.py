# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 13:07:36 2017

@author: anju
"""

"""
Plot the data in the file provided through the URL
"""

import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")

plt.plot(data)

plt.show()

