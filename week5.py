# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:28:17 2016

@author: kalpoffer
"""



######################### LOADER FROM FILE #############################

file = open("/home/kalpoffer/Downloads/daa/tree.txt").read()
#file = open("/home/kalpoffer/Downloads/daa/tree2.txt").read()
#file = open("/home/kalpoffer/Downloads/daa/tree3.txt").read()
#file = open("/home/kalpoffer/Downloads/daa/tree4.txt").read()
#file = open("/home/kalpoffer/Downloads/daa/tree5.txt").read()
########### METHOD #######################

loader = []
i=0
for e in file.split("\n"):
    e = e.split("\t")
    loader.append([])
    
    for element in e:
        element = element.split(",")
        #print element
        if(element != ['']):
            loader[i].append(element)
    
    i = i+1

######################## OOP ###############################

class node(object):
    
    
    def __init__(self, value, explored):
        
        self.value = value
        self.explored = explored
    
    def returnValue(self):
        return self.value

    def isExplored(self):
        return self.explored
    
    def Explored(self):
        self.explored = True


class edge(object):
    
    def __init__(self, node1, node2, weight):
        
        self.node1 = node1
        self.node2 = node2
        self.weight = weight
    
    def returnNode1(self):
        return self.node1
    
    def returnNode2(self):
        return self.node2
        
    def returnValue1(self):
        return self.node1.returnValue()
    
    def returnValue2(self):
        return self.node2.returnValue()
    
    def returnWeight(self):
        return self.weight
    
    def returnValues(self):
        return (self.node1.returnValue(), self.node2.returnValue())
        
class tree(object):
    
    def __init__(self,arraynode,arrayedge):
        self.arraynode = arraynode
        self.arrayedge = arrayedge
    
    def RAE(self):
        return self.arrayedge
        
    def RAN(self):
        return self.arraynode
    
    def PAN(self):
        for e in self.arraynode:
            print(e.returnValue())

    def PAE(self):
        for e in self.arrayedge:
            print((e.returnValue1(), e.returnValue2(), e.returnWeight()))
            
    def RAW(self):
        
        k = []
        for e in self.arrayedge:
            k.append(e.returnWeight())
            
        return k
        
    def ConnectedNodes(self,node):
        u = []
        for e in self.arrayedge:
            #print e.returnValues()
            if(e.returnValue1() == node):
                u.append(e)
        
        return u

######################### METHOD #########################################        
        
def SPF(Graph,n):
    
    Start = Graph.RAN()[0]
    
    X = [] #the nodes previously seen
    
    A = {} #the heap which contains the weight os the shorest path
    A.__setitem__(Start.returnValue(),0)
    
    i=0
    
    while(i < len(A.keys())):
        
        
        connected_nodes = Graph.ConnectedNodes(A.keys()[i])
        for e in connected_nodes:
            
            if(e.returnValue2() not in A.keys()):
                X.append(e)
                A.__setitem__(e.returnValue2(), e.returnWeight() + A[e.returnValue1()])
            elif(e.returnWeight() + A[e.returnValue1()] < A[e.returnValue2()]):
                A.__setitem__(e.returnValue2(), e.returnWeight() + A[e.returnValue1()])
                i = 0
                
        
        i = i+1
        

    if(n not in A.keys()):
       A.__setitem__(n,1000000)
    
    return A
####################### CREATION TREE ################################


def creator(array):
    nodes = []
    edges = []
    for e in array:
        for element in e:
            if(len(element) == 1):
                nodes.append(node(int(element[0]), False))
            else:
                edges.append(edge(node(int(e[0][0]), False), node(int(element[0]), False), int(element[1])))
    
    nodes.append(node(len(nodes)+1, False))
    return tree(nodes,edges)
    
########################################################

g = creator(loader)                    
k = SPF(g,6)

print(k)