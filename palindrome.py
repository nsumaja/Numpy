# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 17:43:19 2019

@author: NayiniS
"""

def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    rev = reverse(s) 
  
  
    if (s == rev): 
        return True
    return False
  
  

s = "MADAM"
ans = isPalindrome(s) 
  
if ans == 1: 
    print("Yes") 
else: 
    print("No") 