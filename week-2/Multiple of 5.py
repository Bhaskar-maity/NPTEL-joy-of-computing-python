# -*- coding: utf-8 -*-
"""
@author: bhaskar
"""
'''
Programming Assignment-2: Multiple of 5
Due on 2019-08-22, 23:59 IST
Given a list A of numbers (integers), you have to print those numbers which are not multiples of 5.

Input Format:

The first line contains the numbers of list A separated by a space.

Output Format:

Print the numbers in a single line separated by a space which are not multiples of 5.

Example:

Input:

1 2 3 4 5 6 5

Output:

1 2 3 4 6

Explanation:
Here the elements of A are 1,2,3,4,5,6,5 and since 5 is the multiple of 5, after removing them the list becomes 1,2,3,4,6.
'''
a=[int(i) for i in input().split(" ")]
l=[]
for j in a:
  if j%5!=0:
    l.append(j)
for k in range(len(l)):
  if k!=len(l)-1:
    print(l[k],end=" ")
  else:
    print(l[k],end="")
