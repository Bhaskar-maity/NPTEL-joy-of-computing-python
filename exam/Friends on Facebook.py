# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 21:13:18 2020

@author: bhaskar

SET-2: Friends on Facebook
Due on 2019-11-03, 21:00 IST
 In this course we have tested your intelligence based on your programming capabilities. Here is a mathematical puzzle that you can solve using your programming abilities (if possible).


There are N people P1, P2, P3, …, PN having F1, F2, F3, …, FN Facebook friends, respectively. The solution to this problem is finding k = Fi%Fj such that it is maximum over all valid i,j. 


Constraints:

2 <= N <= 105

1 <= Ai <= 109 for each i



Input Format:

The first line contains an integer N

The second line contains N space-separated integers F1, F2, F3, …, FN



Output Format:

Print in a single line the output which is k, the solution to this problem.


Example:

Input:
5
1 2 3 4 5

Output:
4
"""

n=int(input())
f=list(map(int,input().split()))
nf=[]
for i in range(len(f)):
    for j in range(len(f)):
        k=f[i]%f[j]
        nf.append(k)
print(max(nf),end='')