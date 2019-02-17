# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 01:42:43 2018

@author: shrey
"""
     
    
class Solution():
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         
    def height(self, root): 
      
        # base condition when binary tree is empty 
        if root is None: 
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: 
            return True
  
        # for left and right subtree height 
        lh = self.height(root.left) 
        rh = self.height(root.right) 

        # allowed values for (lh - rh) are 1, -1, 0 
        if (abs(lh - rh) <= 1) and self.isBalanced( 
        root.left) is True and self.isBalanced( root.right) is True: 
            return True

        # if we reach here means tree is not  
        # height-balanced tree 
        return False
    
  
root=Solution(1)
root.left = Solution(2) 
root.right = Solution(3) 
root.left.left = Solution(4) 
root.left.right = Solution(5) 
root.right.left = Solution(6) 
root.left.left.left = Solution(7) 

  
if root.isBalanced(root): 
    print('Tree is balanced') 
else: 
    print('Tree is not balanced')