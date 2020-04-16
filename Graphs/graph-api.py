# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 13:43:29 2020

@author: shrey
"""

class UndirectedGraph():
    
    def __init__(self, graph_dict = None):
        
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict
        
    def add_vertex(self, node):
        if node not in self.__graph_dict:
            self.__graph_dict[node] = []
        
        
    def add_edge(self, start, end):
        if start in self.__graph_dict:
            self.__graph_dict[start].append(end)
        else:
            self.__graph_dict[start] = [end]
            
        if end in self.__graph_dict:
            self.__graph_dict[end].append(start)
        else:
            self.__graph_dict[end] = [start]
            
            
    def adjacent_nodes(self, node):
        if node in self.__graph_dict:
            return self.__graph_dict[node]
        else:
            return []
        
    def get_vertices(self):
        return list(self.__graph_dict.keys())
    
    def get_edges(self):
        return self.__generate_edges()
    
    def number_of_edges(self):
        n = 0
        
        for x in self.__graph_dict:
            n += len(self.__graph_dict[x])
            
        return n
    
    
    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges
    
if __name__ == "__main__":

    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }


    graph = UndirectedGraph(g)
    
    print("Vertices of graph:")
    print(graph.get_vertices())
    
    print("Edges of graph:")
    print(graph.get_edges())
    
    print("Add an edge:")
    graph.add_edge("a","z")
    
    print("Vertices of graph:")
    print(graph.get_vertices())
    
    print("Edges of graph:")
    print(graph.get_edges())
