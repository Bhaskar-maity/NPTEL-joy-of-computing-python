# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:56:04 2020

@author: bhaskar

Programming Assignment-2: Maximum Numeric
Due on 2019-10-03, 23:59 IST
Given an alphanumeric string S, extract maximum numeric value from that string. All the alphabets are in lower case. Take the maximum consecutive digits as a single number.

Input Format:
The first line contains the string S.

Output Format:
Print the maximum value

Example:

Input:
23dsa43dsa98

Output:
98

Explanation:
There are three integer values present in the string, 23, 43 and 98. Among these, 98 is the maximum.
"""

import re
ip=input()
l=((re.findall('\d+',ip)))
l=list(map(int,l))
print(max(l),end='')