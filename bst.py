# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 11:07:14 2018

@author: shrey
"""
"""
Binary Search Trees: the right child always has a value less than root and right child always has value greater than root. 
The left and right subtrees are also BSTs.



"""
import numpy as np

class Node:
    def __init__(self, val):
        self.val=val
        self.left = None
        self.right = None
        
    def search(self,root,val):
        if root is None or root.val==val:
            return root
        else:
            if root.val<val:
                return self.search(root.right, val)
            else:
                return self.search(root.left, val)
    """
    check value of node, if value to be inserted is larger, recurse in right tree, else recurse in left tree.
    go to the leaf node and add it to the tree.
    
    """        
    def insert(self,root,node):
        if  root is None:
            root=node
        else:
            if root.val<node.val:
                if root.right is None:
                    root.right=node
                else:
                    self.insert(root.right, node)
            else:
                if root.left is None:
                    root.left=node
                else:
                    self.insert(root.left, node)
                    
    def minValueNode(self, node): 
        current = node 
      
        # loop down to find the leftmost leaf 
        while(current.left is not None): 
            current = current.left  
      
        return current  
                    
    def delete(self, root, key):
        if root is None:
            return root
        
        if root.val<key:
            root.right=self.delete(root.right, key)
        elif root.val>key:
            root.left= self.delete(root.left, key)
        else:
            #zero or one children
            if root.left is None:
                temp=root.right
                root=None
                return temp
            elif root.right is None:
                temp=root.left
                root=None
                return temp
            
            #two children case
            #Min value node can be taken from the min value of the right subtree
            temp=self.minValueNode(root.right)
            root.val=temp.val
            root.right=self.delete(root.right, key)
        return root
                    
    def inorder(self, root): 
        if root: 
            self.inorder(root.left) 
            print(root.val) 
            self.inorder(root.right) 
            
r = Node(50) 
r.insert(r,Node(30)) 

#r.inorder(r)  

r.insert(r,Node(20)) 
r.insert(r,Node(40)) 
r.insert(r,Node(70)) 
r.insert(r,Node(60)) 
r.insert(r,Node(80)) 
  
# Print inoder traversal of the BST 
r.inorder(r)   

#ret=r.search(r,20)  
#if ret == None:
#    print("No")
#else:
#    print("Yes")
print("delete")
r.delete(r, 30)
r.inorder(r)
    
    
            
    
            
                    

                    
        
    
