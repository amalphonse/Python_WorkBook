# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 13:03:38 2017

@author: anju
"""
"""
Question: Write a script that detects and prints out your monitor resolution.
"""

from screeninfo import get_monitors


monitor_width = get_monitors()[0].width
monitor_height = get_monitors()[0].height
print("Monitor Width: %d, Monitor Height: %d" % (monitor_height,monitor_width))
                             