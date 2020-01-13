# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 21:08:03 2020

@author: bhaskar

Programming Assignment-1: Holes
Due on 2019-10-24, 23:59 IST
Let us assume paper as the plane and a letter as a curve on the plane, then each letter divides the plane into regions. For example letters "A", "D", "O", "P", "R" divide the plane into two regions so we say these letters each have one hole. Similarly, letter "B" has two holes and letters such as "C", "E", "F", "K" have no holes. We say that the number of holes in the text is equal to the total number of holes in the letters of the text. Write a program to determine how many holes are in a given text.

Input Format:
The only line contains a non-empty text composed only of uppercase letters of English alphabet.

Output Format:
output a single line containing the number of holes in the corresponding text.

Example-1

Input:
DRINKEATCODE

Output:
5


Explanation:
D R A O D has one hole hence total number of holes in the text is 5.
"""

ip=input()
c=0
H1=["A","D","O","P","R"]
H2=["B"]

for i in ip:
    if i in H1:
        c+=1
    elif i in H2:
        c=c+2
print(c,end="")