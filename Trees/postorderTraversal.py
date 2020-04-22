# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 12:53:32 2020

@author: shrey
"""

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        postorder = []
        
        if root is None:
            return []
        
        postorder += self.postorderTraversal(root.left)
        postorder += self.postorderTraversal(root.right)
        postorder += [root.val]
            
        return postorder