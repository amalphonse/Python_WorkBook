# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 10:46:40 2017

@author: anju
"""

#csv to database 

import sqlite3
import pandas

df = pandas.read_csv("ten-more-countries.txt")
print(df)
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

for index,rows in df.iterrows():
    print(rows["Country"],rows["Area"])
    conn.execute("INSERT INTO countries values (NULL,?,?,NULL)",(rows["Country"],rows["Area"]))

conn.commit()
conn.close()