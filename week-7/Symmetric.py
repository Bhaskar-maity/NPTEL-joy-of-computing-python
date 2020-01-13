# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:45:32 2020

@author: bhaskar

Programming Assignment-2: Symmetric
Due on 2019-09-19, 23:59 IST
Given a square matrix of N rows and columns, find out whether it is symmetric or not.

Input Format:
The first line of the input contains an integer number n which represents the number of rows and the number of columns.
From the second line, take n lines input with each line containing n integer elements with each element separated by a space.

Output Format:
Print 'YES' if it is symmetric otherwise 'NO'

Example:

Input:
2
1 2
2 1

Output:
YES
"""

"""

@author: descentis
"""

def isSymmetric(mat, N): 
    for i in range(N): 
        for j in range(N): 
            if (mat[i][j] != mat[j][i]): 
                return False
    return True
   

a = int(input())


m = []
for i in range(1,a+1):    
    l = list(map(int, input ().split ()))
    m.append(l)
if (isSymmetric(m, a)): 
    print("YES")
else: 
    print("NO")