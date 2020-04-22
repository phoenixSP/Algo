# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:19:23 2020

@author: shrey
"""

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        
        queue = []
        ans = []
        
        if root: 
            queue.append(root)
            
        while len(queue):
            levelNodes = len(queue)
            levelNodesList = []
            
            while levelNodes:
                
                node = queue.pop(0)
                levelNodesList.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:  
                    queue.append(node.right)
                levelNodes -= 1
                
            ans.append(levelNodesList)
            
        return ans