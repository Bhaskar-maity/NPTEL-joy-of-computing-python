# -*- coding: utf-8 -*-
"""

@author: bhaskar
"""

'''
Programming Assignment-2: Small
Due on 2019-08-22, 23:59 IST
Given two numbers (integers) as input, print the smaller number.

Input Format:
The first line of input contains two numbers separated by a space

Output Format:
Print the smaller number

Example:

Input:
2 3

Output:
2
'''

p=input() #take input as string
l,d=p.split() #split input
l=int(l)
d=int(d)
if l>d:
  print(d,end="")
else:
  print(l,end="")