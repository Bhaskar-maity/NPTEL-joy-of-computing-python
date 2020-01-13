# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 21:05:25 2020

@author: bhaskar

Programming Assignment-2: String Sort
Due on 2019-10-17, 23:59 IST
Write a program that accepts a comma-separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

Input Format:
The first line of input contains words separated by the comma.

Output Format:
Print the sorted words separated by the comma.

Example:

Input:
without,hello,bag,world

Output:
bag,hello,without,world

"""

x=list(input().split(","))
x.sort()
print(*x,sep=",",end="")