# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:41:53 2020

@author: bhaskar

Programming Assignment-3: Functions
Due on 2019-09-12, 23:59 IST
Given an integer number n, define a function named printDict() which can print a dictionary where the keys are numbers between 1 and n (both included) and the values are square of keys.
The function printDict() doesn't take any argument.

Input Format:
The first line contains the number n.

Output Format:
Print the dictionary in one line.

Example:

Input:
5

Output:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

NOTE: You are supposed to write the code for the function printDict() only. The function has already been called in the main part of the code.
"""
def printDict():
  d={}
  for i in range (1,n+1):
    d.update({i:i*i})
  print(d,end="")
n=int(input())
printDict()
printDict()

