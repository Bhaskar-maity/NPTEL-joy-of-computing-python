# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:58:22 2020

@author: bhaskar

Programming Assignment-1: Special Character
Due on 2019-10-10, 23:59 IST
Given a string S, check whether it contains any special character or not. Print 'YES' if it does else 'NO'.

Input Format:

The first line contains the string S

Output Format:

Print 'YES' or 'NO'

Example:

Input:
Hi$my*name

Output:
YES
"""

import string
invalidChars = set(string.punctuation)
word=input()
if any(char in invalidChars for char in word):
    print ("YES",end='')
else:
    print ("NO",end='')
