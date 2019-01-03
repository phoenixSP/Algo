# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 08:22:38 2018

@author: shrey
"""

class Solution:

    def longestConsecutive(self, nums):
        s=set()
        res=0
        for element in nums:
            s.add(element)
        
        for i in range(len(nums)):
            ele=nums[i]
            if (ele-1) not in s:
                while ele in s:
                    ele+=1
                    
                res=max(res,ele-nums[i])
        return res

    
arr=[1, 9, 3, 10, 4, 20, 2]
sol=Solution()
res=sol.longestConsecutive(arr)
print(res)