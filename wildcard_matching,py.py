# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 03:31:35 2018

@author: shrey
"""

import numpy as np

'''
?= only one character
*= zero or more character

T[i][j]={ T[i-1][j-1] if str[i]=pattern[j] || pattern[j]='?' ;
          T[i-1][j] if pattern[j]=='*';
          False}

'''


class Solution:

    def isMatch(self, s, p):
        T = [[False] * (len(p)+1) for _ in range(len(s)+1)]
        #T=np.zeros(shape=(len(s)+1,len(p)+1))
            
#        if p[0]=="*":
#            T[0][1]=True
        
        T[0][0]=True    
        for i in range(1,len(p)+1):
            if p[i-1]=="*":
                T[0][i]=T[0][i-1]
       
        
        for i in range(1, len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=="?" or p[j-1]==s[i-1]:
                    T[i][j]=T[i-1][j-1]
                elif p[j-1]=="*":
                    T[i][j]=T[i-1][j] or T[i][j-1]
                else:
                    T[i][j]=False
        return T[len(s)][len(p)], T
    
s="aa"
p="*"

sol=Solution()

flag, T =sol.isMatch(s,p)
if flag==True:
    print("Match")
    
            
            
            
        
        
        
    