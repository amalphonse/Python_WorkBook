# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 14:53:14 2017

@author: anju
"""

"""
Question: Generate a password of 6 random alphanumeric characters
"""

import random

characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passwd_chsn = random.sample(characters,6)
passwd = "".join(passwd_chsn)
print("The password is %s: " %(passwd))