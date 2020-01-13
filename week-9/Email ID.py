# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:57:12 2020

@author: bhaskar

Programming Assignment-3: Email ID
Due on 2019-10-03, 23:59 IST
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

Input Format:
The first line of the input contains an email address.

Output Format:
Print the company name in single line.

Example;

Input:
john@google.com

Output:
google
"""

ip=input()
x=ip.index("@")
print(ip[x+1:len(ip)-4],end='')