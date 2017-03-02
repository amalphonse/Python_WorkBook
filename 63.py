# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 18:43:45 2017

@author: anju
"""

"""
Question: Create a program that once executed the programs prints Hello  instantly first, then it prints it after 1 second, then after 2, 3, and then the program prints out the message "End of the Loop" and stops.
"""

import time

i=0

while True:
    i=i+1
    print("Hello")
    if i > 3:
        print("End of Loop")
        time.sleep(i)
        break
    
