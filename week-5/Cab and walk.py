# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:26:59 2020

@author: bhaskar

Programming Assignment-1: Cab and walk
Due on 2019-09-05, 23:59 IST
Arun is working in an office which is N blocks away from his house. He wants to minimize the time it takes him to go from his house to the office.
He can either take the office cab or he can walk to the office.
Arun's velocity is V1 m/s when he is walking. The cab moves with velocity V2 m/s but whenever he calls for the cab, it always starts from the office, covers N blocks, collects Arun and goes back to the office.
The cab crosses a total distance of N meters when going from office to Arun's house and vice versa, whereas Arun covers a distance of (2–√∗N) while walking.
Help Arun to find whether he should walk or take a cab to minimize the time.

Input Format:
A single line containing three integer numbers N, V1, and V2 separated by a space.

Output Format:
Print 'Walk' or 'Cab' accordingly

Constraints:

1<=V1, V2 <=100

1<=N<=200

Example-1:

Input:
5 10 15

Output:
Cab

Example-2:

Input:
2 10 14

Output:
Walk
"""
N,v1,v2=input().split(" ")
N,v1,v2=int(N),int(v1),int(v2)
t1=(2*N)/v2
t2=(2**0.5)/v1
if t1>t2:
  print("Walk",end="")
else:
  print("Cab",end="")
