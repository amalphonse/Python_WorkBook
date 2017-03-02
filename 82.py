# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 12:55:50 2017

@author: anju
"""
"""
Use Python to calculate the distance in kilometers between Jupiter and Sun on January 1, 1230.
"""
import ephem

jupiter = ephem.Jupiter()
jupiter.compute('1230/1/1')
distance_au = jupiter.sun_distance
print(distance_au * 149597870.691)

