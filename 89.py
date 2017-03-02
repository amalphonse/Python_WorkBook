# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 19:14:57 2017

@author: anju
"""

import sqlite3

conn= sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute("SELECT country FROM countries WHERE area >= 2000000")
rows = cursor.fetchall()
print(rows)
for i in rows:
    print(i[0])