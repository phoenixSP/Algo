# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 12:06:42 2019

@author: shrey
"""
from collections import defaultdict

class Directed_Graph:
    def __init__(self,adj_list=None, vertices=0):
        if adj_list==None:
            adj_list=defaultdict(list)
        self.__adj_list=adj_list
        self.__no_of_vertices=vertices
        
    def add_edge_directed(self,src,dst): #undirectedgraph
        if src in self.__adj_list:
            self.__adj_list[src].append(dst)
        else:
            self.__adj_list[src]=[dst]

    def DFS_Util(self,v,visited):
        visited[v]=True
        print(v, end=" ")
        
        for i in self.__adj_list[v]:
            if visited[i]==False:
                self.DFS_Util(i, visited)
                
    def DFS(self,v):
        visited=[False]*self.__no_of_vertices
        self.DFS_Util(v,visited)    
    
    def BFS(self,s):
        queue=[]
        visited=[False]*self.__no_of_vertices
        
        queue.append(s)
        visited[s]=True
        
        while queue:
            s=queue.pop(0)
            print(s,end=" ")
            
            for i in self.__adj_list[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
                    
    def topological_sort_Util(self,v,visited, stack):
        visited[v]=True
        for i in self.__adj_list[v]:
            if visited[i]==False:
                self.topological_sort_Util(i,visited,stack)
        
        stack.insert(0,v)

                
    def topological_sort(self): #for dags
        visited=[False]*self.__no_of_vertices
        stack=[]
        
        for i in range(len(self.__adj_list)):
            if visited[i]==False:
                self.topological_sort_Util(i,visited,stack)
                
        print(stack)              
        
    def printList(self):
        print(self.__adj_list)
                
    def detect_cycle_directed_util(self,v,visited,stack):
        stack[v]=True
        visited[v]=True
        
        for i in self.__adj_list[v]:
            if visited[i]==False:
                if self.detect_cycle_directed_util(i,visited,stack)==True:
                    return True
            elif stack[i]==True:
                return True
        
        stack[v]=False
        return False
    
    def detect_cycle_directed(self):
        visited=[False]*self.__no_of_vertices
        stack=[False]*self.__no_of_vertices
        
        for i in range(self.__no_of_vertices):
            if visited[i]==False:
                if self.detect_cycle_directed_util(i,visited, stack)==True:
                    return True
        return False    
    
    def detect_cycle_color_util(self,v,color):
        color[v]="GRAY"
        for i in self.__adj_list[v]:
            if color[i]=="GRAY":
                return True
            if color[i]=="WHITE" and self.detect_cycle_color_util(i,color)==True:
                return True
            
            color[v]="BLACK"
            return False
    
    def detect_cycle_color(self):
        color=["WHITE"]*self.__no_of_vertices
        for i in range(self.__no_of_vertices):
            if color[i]=="WHITE":
                if self.detect_cycle_color_util(i,color)==True:
                    return True
        return False
        
graph2=Directed_Graph(vertices=3)
graph2.add_edge_directed(0,1)
graph2.add_edge_directed(2,0)
graph2.add_edge_directed(2,2)

graph2.printList()

graph2.BFS(0)

graph2.topological_sort()

if graph2.detect_cycle_color()==True:
    print("cycle")
else:
    print("no cycle")        
        
        
        