# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 21:44:34 2019

@author: shrey
"""
from collections import defaultdict

class AdjNode:
    def __init__(self,data):
        self.data=data
        self.next=None

#Implementing an undirected graph    
class Graph:
#    #This method tries to imitate the c++ way of implementionn of Graphs, but it is 
#    #not essential. So better way is to implement using dictionary. 
#    def __init__(self,vertices):
#        self.no_of_vertices=vertices
#        self.adjacency_list=[None]*self.no_of_vertices
#        
#    def add_edge(self,src,dst):
#        node=AdjNode(dst)
#        node.next=self.adjacency_list[src]
#        self.adjacency_list[src]=node
#        
#        node=AdjNode(src)
#        node.next=self.adjacency_list[dst]
#        self.adjacency_list[dst]=node
#        
#    def print_graph(self):
#        for i in range(self.no_of_vertices):
#            print("Adjacency list of vertex",str(i),"is: head",end="")
#            temp=self.adjacency_list[i]
#            while temp:
#                print("-> ",str(temp.data),end="")
#                temp=temp.next
#                
#            print()
    
    def __init__(self,adj_list=None, vertices=0):
        if adj_list==None:
            adj_list=defaultdict(list)
        self.__adj_list=adj_list
        self.__no_of_vertices=vertices
        
    def add_edge_undirected(self,src,dst): #undirectedgraph
        if src in self.__adj_list:
            self.__adj_list[src].append(dst)
        else:
            self.__adj_list[src]=[dst]
            
        if dst in self.__adj_list:
            self.__adj_list[dst].append(src)
        else:
            self.__adj_list[dst]=[src]

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
                    
        
    def printList(self):
        print(self.__adj_list)
                
    def detect_cycle_util(self,v,visited,parent):
        visited[v]=True
        
        for i in self.__adj_list[v]:
            if visited[i]==False:
                if self.detect_cycle_util(i,visited,v)==True:
                    return True
            elif parent!=i:
                return True
        
        return False
    
    def detect_cycle(self):
        visited=[False]*self.__no_of_vertices
        
        for i in range(self.__no_of_vertices):
            if visited[i]==False:
                if self.detect_cycle_util(i,visited, -1)==True:
                    return True
        return False
    
graph = Graph(vertices=5) 
graph.add_edge_undirected(1,0) 
graph.add_edge_undirected(0,2) 
graph.add_edge_undirected(2,0) 
graph.add_edge_undirected(0,3)
graph.add_edge_undirected(3, 4) 
  
#graph.print_graph()      

if graph.detect_cycle()==True:
    print("cycle")
else:
    print("no cycle")


