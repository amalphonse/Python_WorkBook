# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 14:07:51 2017

@author: Anju
"""

"""
Data Writer App
"""

from flask import Flask, render_template, request

app=Flask(__name__)

html = """
<div class="form>
    <form action="{{url_for('sent')}}" method="POST">
                    <input title="Your email address." 
    </form>
</div>
"""