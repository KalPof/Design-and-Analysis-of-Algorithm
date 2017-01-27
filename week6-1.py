# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 16:48:38 2016

@author: kalpoffer
"""

file = open("/home/kalpoffer/Downloads/daa/_6ec67df2804ff4b58ab21c12edcb21f8_Median.txt").read()


k = []
for e in file.split("\n"):
    if(e != ""):
        k.append(int(e))

#print k
class Node(object):
    
    def __init__(self,value):
        self.value=value
        self.right = None
        self.left = None
        self.Parental = None
    
    def setRight(self,value):
        self.right = value
    
    def setLeft(self,value):
        self.left = value
    
    def setParental(self,value):
        self.parental = value
    
    def getRight(self):
        return self.right
    
    def getLeft(self):
        return self.left
    
    def getParental(self):
        return self.parental
    
    def getValue(self):
        return self.value


class Tree(object):
    
    tree = []
    def __init__(self,size):
        self.tree = [Node(0)]*size
        self.n = 0
    
    def insert(self,value):
        
        #print("here")
        #print("the value passed is " + str(value))
        nd = Node(value)
        
        if(self.n == 0):
            self.tree[self.n] = nd
            #print("the value at the root (0) is " + str(nd.getValue()))
        else:
            
            current = self.tree[0]
            #print("the value at the root is " + str(current.getValue()))
            while(current.getLeft() != None or current.getRight() != None):
                
                #print("is " + str(current.getValue()) + " less than " + str(value) + "?")
                if(current.getValue() > value):
                    #print("no. going left. Value: " + str(current.getValue()))
                    if(current.getLeft() == None):
                        break
                    current = current.getLeft()
                    
                else:
                    #print("yes. going right. Value: " + str(current.getValue()))
                    #print(current.getValue())
                    if(current.getRight() == None):
                        break
                    current = current.getRight()
                    
            
            #print("")
            #print("cycle 2")
            #print("is " + str(current.getValue()) + " less than " + str(value) + "?")
            if(current.getValue() > value):
                #print("no. going left. Value: " + str(current.getValue()))
                current.setLeft(nd)
                #print("now " + str(current.getValue()) + " has a left: " + str(nd.getValue()) )
            else:
                #print("yes. going right. Value: " + str(current.getValue()))
                current.setRight(nd)
                #print("now " + str(current.getValue()) + " has a right: " + str(nd.getValue()) )
            
            #print("")
            nd.setParental(current)
            self.tree[self.n] = nd
        self.n = self.n + 1
        
    def getMax(self):
        
        current = self.tree[0]
        #print(current.getValue())
        while(current.getRight() != None):
            current = current.getRight()
            #print(current.getValue())
        
        return current.getValue()
    
    def getMinR(self):
        current = self.tree[0].getRight()
        #print(current.getValue())
        while(current.getLeft() != None):
            
            current = current.getLeft()
            #print(current.getValue())
           
        return current.getValue()
    
    def getMin(self):
    
        current = self.tree[0]
        #print(current.getValue())
        while(current.getLeft() != None):
            
            current = current.getLeft()
            #print(current.getValue())
           
        return current.getValue()
    
    #def PAR(self):
        
    def retTree(self):
        for e in self.tree:
            print e


t = Tree(len(k))
for e in k:
   t.insert(e)

print(t.getMin())
#print("")
print(t.getMax())
print(t.getMinR())
#print("")
#t.getMinR()