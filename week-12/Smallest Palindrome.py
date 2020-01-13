# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 21:08:50 2020

@author: bhaskar

Programming Assignment-2: Smallest Palindrome
Due on 2019-10-24, 23:59 IST
Given a string S having characters from English alphabets ['a' - 'z'] and '.' as the special character (without quotes). 
Write a program to construct the lexicographically smallest palindrome by filling each of the faded character ('.') with a lower case alphabet.

Definition:
The smallest lexicographical order is an order relation where string s is smaller than t, given the first character of s (s1 ) is smaller than the first character of t (t1 ), or in case they
are equivalent, the second character, etc.

For example "aaabbb" is smaller than "aaac" because although the first three characters
are equal, the fourth character b is smaller than the fourth character c. 

Input Format: 
String S

Output Format: 
Print lexicographically smallest palindrome after filling each '.' character, if it
possible to construct one. Print -1 otherwise.

Example-1

Input:
a.ba

Output:
abba


Example-2:

Input:
a.b

Output:
-1

Explanation: 
In example 1, you can create a palindrome by filling the '.' character by 'b'.
In example 2, it is not possible to make the string s a palindrome.
"""

# Python3 for constructing smallest palindrome 
  
# function for printing palindrome 
def constructPalin(string, l): 
    string = list(string) 
    i = -1
    j = l 
    
    # iterate till i<j 
    while i < j: 
        i += 1
        j -= 1
  
        # continue if str[i]==str[j] 
        if (string[i] == string[j] and 
            string[i] != '.'): 
            continue
  
        # update str[i]=str[j]='a' if both are '.' 
        elif (string[i] == string[j] and 
              string[i] == '.'): 
            string[i] = 'a'
            string[j] = 'a'
            continue
  
        # update str[i]=str[j] if only str[i]='.' 
        elif string[i] == '.': 
            string[i] = string[j] 
            continue
  
        # update str[j]=str[i] if only str[j]='.' 
        elif string[j] == '.': 
            string[j] = string[i] 
            continue
  
        # else print not possible and return 
        print("-1") 
        return "" 
    return ''.join(string) 

ip=input()
print(constructPalin(ip, len(ip)))
  
