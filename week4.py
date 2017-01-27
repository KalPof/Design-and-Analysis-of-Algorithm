# -*- coding: utf-8 -*-

import gc
"""
Created on Thu Nov 24 19:34:06 2016

@author: kalpoffer
"""
def printer(array):
    for e in array:
        print e.returnValue()            
######################### FILE OPENER #######################

file1 = open("/home/kalpoffer/Downloads/daa/w4/grapht1.txt").read()
#file1 = open("/home/kalpoffer/Downloads/daa/w4/graph2.txt").read()
#file1 = open("/home/kalpoffer/Downloads/daa/w4/graph3.txt").read()
#file1 = open("/home/kalpoffer/Downloads/daa/w4/graph4.txt").read()
#file1 = open("/home/kalpoffer/Downloads/daa/w4/graph5.txt").read()
#file1 = open("/home/kalpoffer/Downloads/daa/w4/graph.txt").read()
#file1 = open("/home/kalpoffer/Downloads") those are used for tests

########## LOADER FOR TESTS ##################

graph = []

for e in file1.split("\n"):
        graph.append(e)
        
        del(e)
        
c = []

print("step 2")
for e in graph[0:len(graph)]:

        c.append([e.split(" ")[0],e.split(" ")[1]])
        
        del(e)

del(graph)
gc.collect()
w = []
print("step 3")
i = 0
for r in c:
    
    if(len(w) == 0):
        w.append([r[0],[r[1]]])
    elif(w[len(w)-1][0] == r[0]):
        w[len(w)-1][1].append(r[1])
    else:
        w.append([r[0],[r[1]]])
    
    del(r)

del(c)
gc.collect()
print("step 4")    
  
######################## OOP GRAPH CREATION ######################

class Node(object):
    
    label = 0
    def __init__ (self, value, discovered):
        self.value = int(value)
        self.discovered = False
        self.label = int(value)
    
    def setLabel(self,label):
        self.label = label
    
    def returnLabel(self):
        return self.label
        
    def explored(self):
        self.discovered = True
    
    def isExplored(self):
        return self.discovered
        
    def unexplored(self):
        self.discovered = False
    
    def returnValue(self):
        return self.value

class Edge(object):
    
    def __init__(self,node1,node2):
        self.node1 = node1
        self.node2 = node2
    
    def returnNodes(self):
        return (self.node1.returnValue(), self.node2.returnValue())
    
    def returnNode1(self):
        return self.node1.returnValue()
    
    def returnNode2(self):
        return self.node2.returnValue()

class Graph(object):
    
    def __init__ (self,ArrayOfNodes, ArrayOfEdges):
        self.ArrayOfNodes = ArrayOfNodes 
        self.ArrayOfEdges = ArrayOfEdges
    
    def RAN(self): #stands for returnArrayNodes
        return self.ArrayOfNodes 
        
    def PAN(self): #stands for PrintAllNodes
        for e in self.ArrayOfNodes:
            print e.returnValue()
            
    def SAU(self): #Stands for SetAllUnexplored. All the nodes of arrayOfnodes are now undiscoverd
        for e in self.ArrayOfNodes:
            e = e.unexplored()    
            
    def PAE(self): #stands for PrintAllEdges
        for e in self.ArrayOfEdges:
            print e.returnNodes()
            
    def InvertThis(self):
        
        newEdges = []
        for e in self.ArrayOfEdges:
            newEdges.append(Edge(Node(e.returnNode2(), False),Node(e.returnNode1(), False)))
            del(e)
        
        g = Graph(self.RAN(), newEdges)
        return g  
        
    def RAE(self): #stands for returnAllEges
        return self.ArrayOfEdges
        
    def RSN(self,Value): #stands for returnSpecificNode
        for e in self.ArrayOfNodes:
            
            if(e.returnValue() == Value):
                return e
                
    def returnConnectedNodes(self,Node):
        add = []
        for e in self.ArrayOfEdges:
            if(Node.returnValue() ==  e.returnNode1()):
                add.append(self.RSN(e.node2.returnValue()))
        
        return add
    
    def PAD(self):
        for e in self.ArrayOfNodes:
            print(str(e.returnValue()) + " " + str(e.isExplored()))
    ############################### SEARCH METHODS #############################
     
    def BFS(self, Start_Node):
        
        """
        # the breadth-first search is search graph algorithm based
        #on the presence of multiple layers of nodes in the graph to search into
        # A layer is composed of all the nodes related to the current node
        # but which aren't on the same layer
        """
        
        #first of all, we need to set all the nodes in the graph unexplored
        # if it's node. go on
        
        #let's set the start node explored
        
        Start_Node.explored()
        
        #create the instance of a queue, or an array which travels all down
        #like a queue
        
        #print(Start_Node.returnValue())
        queue = []
        #print(queue)
        #add the start node to the queue
        
        queue.append(Start_Node)
        
        #now the start node is in the position 0 of the queue
        #begin a while lopp until the queue is not empty
        
        while(len(queue) != 0):
            
            v = queue.pop(0)
            connected_nodes = self.returnConnectedNodes(v)
            
            print("the nodes connected to " + str(v.returnValue()) + " are: ")
            print(connected_nodes)
            for e in connected_nodes:
                
                if(e.isExplored() == False):
                    e.explored()
                    queue.append(e)
                
                
    
        
    def DFS(self, Start_Node):
    
        """
        The depth-first search algorithm, is an algorithm based upon
        the finding of all nodes in a more aggressive way compared to the breadth-first
        kind of searching.
        This algorithm works usinif(n1.returnValue() != nodes[len(nodes)-1].returnValue()):
            nodes.append(n1)g a deeper search, traveling all the possible
        pathway reachable from a specific node. Here we don't travel by layers
        but we go throught all the graph edge by edge, and we came back only in
        specific situations of the graph (for example, after we've found a sink node)
        """
        
        #as before, we start setting all the nodes as unexplored
        self.SAU()
        
        #now, we set the start node as explored
        Start_Node.explored()
        
        #from here, we simply go "straight on" reaching all the nodes from
        #the current one, and coming back only when needed
        
        #for DFS we need a stack kind of structure, so
        stack = []
        
        #add the start node to the stack
        stack.append(Start_Node)
        
        #iterate until the stack isn't empty
        
        while(len(stack) != 0):
            
            #delete the last added node from the stack, as an usual stack
            v = stack.pop()
            
            #create a cycle which needs to go until all the nodes linked to v
            #aren't discovered
            connected_nodes = self.returnConnectedNodes(v)
            
            print("the nodes connected to " + str(v.returnValue()) + " are: ")
            print(connected_nodes)
            
            for e in connected_nodes:
                if(e.isExplored() == False):
                    
                    e.explored()
                    stack.append(e)
     
############ METHODS ################
     
def createGraph(a):
    
    gc.collect()
    nodes = []
    edges = []
    
    for e in a:
        nodes.append(Node(e[0],False))
        for element in e[1]:
            edges.append(Edge(Node(e[0],False),Node(element, False)))
        
        del(e)
        #gc.collect()
    return Graph(nodes,edges)
    

################## METHODS FOR SCC ##################

def Two_pass_1(Graph):
    
        """
        This is the code for the kosaraju's two pass algorihm, which is
        a really straightforward way to computer and find SCC
        SCC stands for strongly connected components and are, in graphs,
        nodes which points each other, forming a cycle.
        
        In this code, we need to find the 5 biggests SCC in the given graph
        
        The algorithm is structured in 2 passages: 1) the reversing of all the
        edges in the graph, pointing in the opposite direction of the actual
        one 2) the cycle of all the components of the array used to fin the scc
        
        To Compute the algorithm, we need 2 differents instances of DFS.
        The first one aims to give a new labeling for all the nodes in the 
        inverted graph, and the second iteration aims to find the scc 
        """
        
        i = Graph.RAN()[len(Graph.RAN())-1].returnValue()
        
        global emp_array
        emp_array = []
        
        while(i > 2):
            current_node = Graph.RSN(i)
            i = i-1
            if(current_node.isExplored() == False):
                DFS3(Graph,current_node)
        
        k = emp_array
        
        Two_pass_2(Graph,k)
    

def Two_pass_2(Graph,array):
    
    new_Graph = Graph.InvertThis()
    new_Graph.SAU()
    i = len(array)-1
    global emp_array
    emp_array = []
    global t
    t=0
    while(i >= 0):
        current_node = array[i]
        i = i-1
        if(current_node.isExplored() == False):
            emp_array.append(Node(0,False))
            DFS3(new_Graph,current_node)
            
    emp_array.append(Node(0,False))
    t = emp_array
    final = []
    i=0
    for e in t:
            if(e.returnValue() == 0):
                final.append(i)
                i=0
            else:
                i=i+1
    
    final.sort
    final.reverse
    print final[1:]
    

def DFS3(Graph, Start_Node):
        
        
        Start_Node = Graph.RSN(Start_Node.returnValue()) 
        Graph.RSN(Start_Node.returnValue()).explored()
        Start_Node.explored()      
        connected_nodes = Graph.returnConnectedNodes(Start_Node)
        for e in connected_nodes:
            if(e.isExplored() == False):
                DFS3(Graph,e)
        
        global t
        t = t+1
                
        global emp_array
        Start_Node.setLabel(t)

        
        emp_array.append(Start_Node)
        


#### global variables #####
t = 0
emp_array = []
##### creation of the graph #####

gc.collect()
g = createGraph(w)
del(w)
gc.collect()
print("step 5")

label = len(g.ArrayOfNodes)

o = g.InvertThis()
print("step 6")
Two_pass_1(o)


#################### additional methods for debugging  ##################

