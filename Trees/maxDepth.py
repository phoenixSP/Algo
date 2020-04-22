# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:57:10 2020

@author: shrey
"""

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        #bottom up approach
        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        """
        #bottom down approach
        def util(root, depth):
            if root is None:
                return

            if root.left is None and root.right is None:
                self.answer = max(self.answer, depth)

            util(root.left, depth + 1)
            util(root.right, depth + 1)

        util(root, 1)

        return self.answer
        """