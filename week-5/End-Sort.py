# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:34:04 2020

@author: bhaskar

Programming Assignment-2: End-Sort
Due on 2019-09-05, 23:59 IST
Given a list A of N distinct integer numbers, you can sort the list by moving an element to the end of the list. Find the minimum number of moves required to sort the list using this method in ascending order. 

Input Format:
The first line of the input contains N distinct integers of list A separated by a space.

Output Format
Print the minimum number of moves required to sort the elements.

Example:

Input:
1 3 2 4 5

Output:
3

Explanation:
In the first move, we move 3 to the end of the list. In the second move, we move 4 to the end of the list, and finally, in the third movement, we move 5 to the end.
"""
x=[int(i) for i in input().split()]
x1=sorted(x)
c=0

for i in range(len(x)):
  if x[i]==x1[c]:
    c=c+1
print(len(x)-c,end="")
  

