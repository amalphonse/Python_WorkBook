# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 20:23:32 2017

@author: anju
"""

#Database to CSV convertor

import sqlite3
import pandas

conn= sqlite3.connect("database1.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM countries WHERE area >= 2000000")
rows = cursor.fetchall()
print(rows)
df = pandas.DataFrame.from_records(rows)


df.columns=["Rank","Country","Area","Population"]
print(df)
df.to_csv("countries_bigarea.csv",index=False)
