# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 21:01:52 2020

@author: bhaskar

Programming Assignments-3: Calculate
Due on 2019-10-10, 23:59 IST
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.

Input Format:
A sequence of values for D with each value separated by a comma.

Output Format:
Print the sequence of Q values with each value separated by a comma.

Example:

Input:
100,150,180

Output:
18,22,24
"""

print(','.join(list(map(lambda d:str(round((2*50*int(d)/30)**0.5)),input().split(',')))),end='')
