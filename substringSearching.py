# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 18:32:21 2019

@author: shrey
"""

class stringSearch():
    def __init__(self):
        pass
        
    def hash_function(self,string,q):
        value=0
        for i in range(len(string)):
            value+=ord(string[i])*pow(2,i)
        value=value%q    
        return value        
            
    def rabin_karp(self,string,pattern,q):
        b=len(string)
        s=len(pattern)
        
        hash_pattern=self.hash_function(pattern,q)
        hash_s=self.hash_function(string[:s],q)
        
        j=0
        for i in range(b-s+1):
            if hash_pattern==hash_s:
                if pattern==string[i:s+i]:
                    return i
            else:
                hash_s=((hash_s-ord(string[i])*pow(2,s-1))*2 + ord(string[i+s-1]))%q
        i+=1
        print("this should not print")
        if i==b-s+1:
            return -1
                
                
                
                


sb=stringSearch()
k=sb.hash_function("abc", 97)
#string=
#hash_s=((hash_s-ord(string[i])*pow(2,s-1))*2 + ord(string[i+s]))%q  
ret=sb.rabin_karp("abcde","de",7)
      
        