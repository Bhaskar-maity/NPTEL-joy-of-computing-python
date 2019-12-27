# -*- coding: utf-8 -*-
"""
@author: bhaskar
"""

'''
Programming Assignment-1: Max and Min
Due on 2019-08-22, 23:59 IST
Given a list of numbers (integers), find second maximum and second minimum in this list.

Input Format:

The first line contains numbers separated by a space.

Output Format:

Print second maximum and second minimum separated by a space

Example:

Input:

1 2 3 4 5

Output:

4 2
'''
a=[int(i) for i in input().split(" ")]
a.sort()
if (len(a)==2):
  print(a[0],end=" ")
  print(a[1],end="")
else:
  print(a[len(a)-2],end=" ")
  print(a[1],end="")
