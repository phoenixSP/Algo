# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 18:05:30 2020

@author: shrey
"""

class Solution:

            
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        #preorder method
        
        def util(left_node, right_node):
            if not left_node and not right_node:
                return True

            if not left_node:
                return False
            
            if not right_node:
                return False
            

            bool1 = False
            bool2 = False

            if left_node.val == right_node.val:
                bool1 = util(left_node.left, right_node.right)
                bool2 = util(left_node.right, right_node.left)
                
                if bool1 and bool2:
                    return True
                else:
                    return False
            else: 
                return False
        
        if root:
            return util(root.left, root.right)
        else:
            return True
        """
        
        #level order traversal
        
        if not root:
            return True
        
        if not root.left and not root.right:
            return True

        if not root.left:
            return False

        if not root.right:
            return False
        
        stack = [root.left, root.right]

        while len(stack):
            
            l = stack.pop(0)
            r = stack.pop(0)
            
            #if not l and not r:
             #   return True 
                
            if l or r:
                
                if not l or not r:
                    return False

                if l.val != r.val:
                    return False

                stack.append(l.left)
                stack.append(r.right)
                stack.append(l.right)
                stack.append(r.left)
            
        return True