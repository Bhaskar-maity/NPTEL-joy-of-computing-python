# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 21:06:24 2020

@author: bhaskar

Programming Assignment-3: Push the zero
Due on 2019-10-17, 23:59 IST
Write a Python program to push all zeros to the end of a given list a. The order of the elements should not change.

Input Format:
Elements of the list a with each element separated by a space.

Output Format:
Elements of the modified list with each element separated by a space. After the last element, there should not be any space.

Example:

Input:
0 2 3 4 6 7 10

Output:
2 3 4 6 7 10 0

Explanation:
There is one zero in the list. After pushing it at the end the elements of the list becomes 2 3 4 6 7 10 0. The order of other elements remains the same.
"""

arr=[int(i) for i in input().split(' ')]
n=len(arr)
count=0
for i in range(n): 
        if arr[i] != 0: 
              
            arr[count] = arr[i] 
            count+=1
            
while count < n: 
        arr[count] = 0
        count += 1
for i in range(n):
  if i!=n-1:
    print(arr[i],end=' ')
  else:
    print(arr[i],end='')      