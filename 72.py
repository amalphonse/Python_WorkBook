# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 19:45:00 2017

@author: anju
"""
"""
Question: Create a script that let the user type in a search term and opens
and search on the browser for that term on google.
"""

import webbrowser

query = input("Enter your Google query: ")
url = "https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=%s"%str(query)
webbrowser.open_new(url)
