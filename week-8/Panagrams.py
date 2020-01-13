# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:52:22 2020

@author: bhaskar

Programming Assignment-2: Panagrams
Due on 2019-09-25, 23:59 IST
A panagram is a sentence containing every 26 letters in the English alphabet. Given a string S, check if it is panagram or not.

Input Format:
The first line contains the sentence S.

Output Format:
Print 'YES' or 'NO' accordingly

Example:

Input:
The quick brown fox jumps over the lazy dog

Output:
YES
"""

def checkPangram(s): 
    List = [] 
    # create list of 26 charecters and set false each entry 
    for i in range(26): 
        List.append(False) 
          
    #converting the sentence to lowercase and iterating 
    # over the sentence  
    for c in s.lower():  
        if not c == " ": 
            # make the corresponding entry True 
            List[ord(c) -ord('a')]=True 
              
    #check if any charecter is missing then return False 
    for ch in List: 
        if ch == False: 
            return False
    return True
  
# Driver Program to test above functions 
sentence = input()
  
if (checkPangram(sentence)): 
    print("YES")
else: 
    print("NO")