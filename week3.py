# -*- coding: utf-8 -*-

import random
"""
Created on Sat Nov 19 18:47:34 2016

@author: kalpoffer
"""

#this code is used to create a graph and solve a minimun cut problem out of this graph

#first, the parser from the txt file

my_file = open("/home/kalpoffer/Downloads/graph4.txt").read()

################## LOADER #######################

graph = []
for e in my_file.split("\t"):  
    e = e.split("\n")
    graph.append(e)



######## PARSER ##############

c =[]
i=0
k = []
z=True

for e in graph:
    if(len(e) > 1 or z):
        if(graph[0] == e):
            c.append([e[0]])
            z = False
        else:
            c[i].append(k)
            i=i+1
            c.append([e[1]])
            k=[]
    else:
        if(e[0] != ""):
            k.append(e[0])
        if(c[i] == ["200"]):
            c[i].append(k)
    

######################### CLASSES ########################   

class Node(object):
    
    def __init__(self,value):
        self.value = value
    
    def returnValue(self):
        return self.value
    
class Edge(object):
    
    def __init__(self,node1,node2):
        self.node1 = node1
        self.node2 = node2
    
    def returnfNodes(self):
        return self.node1
    
    def returnlNodes(self):
        return self.node2
    
    def returnEdges(self):
        return (self.node1, self.node2)

class Graph(object):

    def __init__(self,arraynodes,arrayedges):
        self.arraynodes= arraynodes
        self.arrayedges = arrayedges
    
    
    def findEdge(self,node1,node2):
        
        for e in self.arrayedges:
            if(e.returnEdges()[0] == node1 and e.returnEdges()[1] == node2):
                #print "here"
                return e
    def returnNodes(self):
        return self.arraynodes
    
    def returnEdges(self):
        return self.arrayedges
    
    def esn(self):
        for e in self.arraynodes:
            print(e.returnValue())
            
    def noe(self):
        return len(self.arrayedges)
    
    def nov(self):
        return len(self.arraynodes)
    
    def deleteNode(self,node):
        for y in g.arraynodes:
            if(y.returnValue() == node):
                self.arraynodes.remove(y)
    def returnEdgePerNode(self,node1):
        
        part_edges = []
        for e in self.arrayedges:
            if(e.returnEdges()[0] == node1):
                part_edges.append(e)
                #print e.returnEdges()
        
        #print(part_edges)
        return part_edges

    def dualDeleter(self,node1,node2):
        deleter = []
        updater = []
        for e in self.arrayedges:
            
            #print("test 2: " + str(e.returnEdges()) + " " + str(node2))
            
            if(e.returnEdges()[0] == node1 or e.returnEdges()[1] == node1 or
            e.returnEdges()[0] == node2 or e.returnEdges()[1] == node2):
                deleter.append(e)
            else:
                updater.append(Edge(e.returnEdges()[0],node1))
        
        for e in deleter:
            self.arrayedges.remove(e)
            
        self.arrayedges.extend(updater)
        
    def createGraph(self,array):
        Nodes = []
        Edges = []
        for element in array:
    
            Nodes.append(Node(element[0]))

            for e in element[1]:
                Edges.append(Edge(element[0],e))
        
        return Graph(Nodes,Edges)
    
    def createGraph2(self,node,edge):
        return Graph(node,edge)
    
    def mincut(self,g):
    
        while(len(g.returnEdges()) > 2):
            
            rand_edge = random.choice(g.arrayedges)
            node1 = rand_edge.returnfNodes()
            node2 = rand_edge.returnlNodes()
            g.arrayedges.remove(rand_edge)
            g.deleteNode(node2)
            o=[]
            for e in g.returnEdges():

                if(e.returnEdges()[0] == node2): 
                    if(e.returnEdges()[1] != node1):
                        o.append(Edge(node1, e.returnEdges()[1]))
                elif(e.returnEdges()[1] == node2): 
                    if(e.returnEdges()[0] != node1):
                        o.append(Edge(e.returnEdges()[0],node1))
                elif(e.returnEdges()[0] != e.returnEdges()[1]):
                    o.append(e)           
            g.arrayedge = o
        return(len(g.arrayedges))    
           
           

########################## METHODS ############################

del_array = []

"""        
def mincut(g):
    
        while(len(g.arraynodes) > 2):
            
            rand_edge = random.choice(g.arrayedges)
            node1 = rand_edge.returnfNodes()
            node2 = rand_edge.returnlNodes()
            #node1 = str(randint(1,len(g.arraynodes)))
            #node1 = random.choice(g.arraynodes).returnValue()
            #node2 = str(randint(1,len(g.arraynodes)))
            #node2 = random.choice(g.arraynodes).returnValue()
            
"""
            #while(node1 == node2):
            #    #node1 = str(randint(1,len(g.arraynodes)))
            #   #node2 = str(randint(1,len(g.arraynodes)))
"""
            
            #print("the deleted nodes are: " + node1 + " " + node2)
            edge = g.findEdge(node1,node2)
            #print(type(edge))
            #print edge.returnEdges()
            #edge = g.arrayedges[node1,node2]
            g.arrayedges.remove(edge)
            
            #del_array.append([node1,node2,(edge)])
            g.deleteNode(node1)
            
            g.deleteNode(node2)
            #print("cacca")
            
            #g.esn()
            #print("")
            g.arraynodes.append(Node(node1))
            #g.esn()
            
            empty_edge = []
            # print("")
            for e in g.returnEdgePerNode(node1):
                if(node1 != e.returnEdges()[1]):
                    k = Edge(node1,e.returnEdges()[1])
                   # print(k.returnEdges())
                    empty_edge.append(k)
            #print empty
            for e in g.returnEdgePerNode(node2):
                #print
                if(node1 != e.returnEdges()[1]):
                    k = Edge(node1,e.returnEdges()[1])
                    #print(k.returnEdges())
                    empty_edge.append(k)
            #print k
                     
            
            #print(g.arrayedges)
            #print("let's use some prints: first arraynodes ")
            #print(g.arraynodes)
            #g.esn()
            #for k in g.arraynodes:
                #print(k.returnValue())
                
            #print("let's use some prints: second arrayedges before deletion")
            #for k in g.arrayedges:
                #print(k.returnEdges())
                
            g.dualDeleter(node1,node2)
            g.arrayedges.extend(empty_edge)  
            #print("let's use some prints: second arrayedges after deletion")

            #for k in g.arrayedges:
            #    print(k.returnEdges())
                
            #print("let's use some prints: third the deleted elements")
            #print(del_array)
            
            #return the edges of the 2 merged nodes
        
        return(len(g.arrayedges))
"""    

def mincut(g):
    
        while(len(g.getarraynodes()) > 2):
            
            rand_edge = random.choice(g.arrayedges)
            node1 = rand_edge.returnfNodes()
            node2 = rand_edge.returnlNodes()
            g.arrayedges.remove(rand_edge)
            g.deleteNode(node2)
            o=[]
            for e in g.arrayedges:
                if(e.returnEdges()[0] == node2):
                    if(e.returnEdges()[1] != node1):
                        o.append(Edge(node1, e.returnEdges()[1]))
                elif(e.returnEdges()[1] == node2):
                    if(e.returnEdges()[0] != node1):
                        o.append(Edge(e.returnEdges()[0],node1))
                elif(e.returnEdges()[0] != e.returnEdges()[1]):
                    o.append(e)
                    
            g.arrayedges = o
            
            
            for e in g.returnEdgePerNode(node1):
                if(node1 != e.returnEdges()[1]):
                    k = Edge(node1,e.returnEdges()[1])
                    empty_edge.append(k)
                    
            for e in g.returnEdgePerNode(node2):
                if(node1 != e.returnEdges()[1]):
                    k = Edge(node1,e.returnEdges()[1])
                    empty_edge.append(k)
                    
            g.dualDeleter(node1,node2)
            g.arrayedges.extend(empty_edge)
            
            
        return(len(g.arrayedges)) 
        

##### TEST ####
        

"""
Nodes = []
Edges = []
for element in c:
    
    Nodes.append(Node(element[0]))

    for e in element[1]:
        Edges.append(Edge(element[0],e))
"""
##########


g = g.createGraph(c[0:len(c)-1])

k = 15
h = []

for i in range(k):
    h.append(g.mincut(g))


h.sort()
print(h)

