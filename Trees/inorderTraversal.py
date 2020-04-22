# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 12:52:08 2020

@author: shrey
"""

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        inorder = []
        
        if root is None:
            return []
        
        inorder += self.inorderTraversal(root.left)
        inorder += [root.val]
        inorder += self.inorderTraversal(root.right)
        
        return inorder