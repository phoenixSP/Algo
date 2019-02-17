# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 21:29:55 2019

@author: shrey
"""
#Kruskal's algorithm

from collections import defaultdict

class Graph:
    def __init__(self,adj_list=None, vertices=0):
        if adj_list==None:
            adj_list=defaultdict(list)
        self.__adj_list=adj_list
        self.__no_of_vertices=vertices
        
    def add_edge(self,src,dst): #undirectedgraph
        if src in self.__adj_list:
            self.__adj_list[src].append(dst)
        else:
            self.__adj_list[src]=[dst]
            
        if dst in self.__adj_list:
            self.__adj_list[dst].append(src)
        else:
            self.__adj_list[dst]=[src]   
            
            
    def kruskal_MST(self):
        
            
    