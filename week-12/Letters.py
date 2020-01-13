# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 21:09:53 2020

@author: bhaskar

Programming Assignment-3: Letters
Due on 2019-10-24, 23:59 IST
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

Input Format:
The first line of the input contains a statement.

Output Format:
Print the number of upper case and lower case respectively separated by a space.

Example:

Input:
Hello world!

Output:
1 9
"""

ip=input()
up=0
lw=0
for i in ip:
    if i.islower():
        lw+=1
    elif i.isupper():
        up+=1
print(up,lw,sep=" ",end="")