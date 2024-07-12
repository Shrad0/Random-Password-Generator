# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 14:33:21 2024

@author: Shraddha
"""

import random
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "!@#$%^&*()_+-=~:;<>,./?\|"

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters

if lower:
    all += lowercase_letters

if nums:
    all += digits

if syms:
    all += symbols
    
length = 15
amount = 10

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)