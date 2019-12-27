# -*- coding: utf-8 -*-
"""
@author: bhaskar
"""
'''
Programming Assignment-1: Factorial
Due on 2019-08-29, 23:59 IST
Given an integer number n, you have to print the factorial of this number. To know about factorial please click on this link.

Input Format:

A number n.

Output Format:

Print the factorial of n.

Example:

Input:
4

Output:
24
'''
def fact(n):
  if n==1:
    return 1
  else:
    return n*fact(n-1)
n=int(input())
print(fact(n),end="")
