# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 12:46:29 2020

@author: shrey
"""

class Solution:
    
    '''
    def __init__(self):
        self.preorder = []
        
    def util(self, root):
        if root: 
            self.preorder.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)        
        
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.util(root)
        return self.preorder
    '''
    
    
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        preorder = []
        
        if root is None:
            return []
        
        preorder += [root.val]
        preorder += self.preorderTraversal(root.left)
        preorder += self.preorderTraversal(root.right)
        
        return preorder
        