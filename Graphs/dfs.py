# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 20:59:41 2020

@author: shrey
"""

from graph import UndirectedGraph


class DepthFirstPaths:
    
    def __init__(self, graph, s):
        self.dfs(graph, s)
        
    def dfs(self, graph, v):
        
        