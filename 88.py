# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 19:03:52 2017

@author: anju
"""

#Data filter

import pandas

countries_df = pandas.read_csv("countries-by-area.txt")
countries_df["density"] = countries_df["population_2013"]/countries_df["area_sqkm"]
countries_df = countries_df.sort_values(by="density",ascending=False)

for index,row in countries_df[:5].iterrows():
    print(row["country"])