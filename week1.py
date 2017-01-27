# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 18:37:43 2016

@author: kalpoffer
"""

#this is me tryong to implement a quicksort algorithm in python

# the load code is equal the previous methods created by me

my_file = open("/home/kalpoffer/Downloads/intar.txt").read()
vec = []
for e in my_file.split("\n"):
	if(e != ""):
		vec.append(e.strip("\r"))
    #created the vector which contains all the integers from the file

#if i remember well, we use an index k to find a random element into the array
#to which create a pivot kind of structure used to the partition of the array



def quicksort(array, left, right,c):
    
    #print("printing c: " + str(c))
    
    if(left >= right):
        #print("with the return: " + str(c))
        return 
    
    pivot = partition(array, left, right)
    c = c + len(array[left:pivot])
    quicksort(array, left, pivot,c)
    #print("here")
    c = c + len(array[pivot+1:right])
    quicksort(array, pivot+1, right,c)

    return (array,c)

def partition(array, left, right):
    
    piv_item = int(array[left]) #we set the pivot as the first element in the array
    
    i = left+1
    j = left+1 #we set 2 pointers pointing at the same 
    #element of the given array
    
    while(j < right):
        if(int(array[j]) < piv_item): #assuming there're no elements equal all around
            swapper(array, j, i)
            i=i+1
        
        j=j+1
        
    swapper(array, left, i-1)
    #print ("printing j: " + str(j))
    #k = k+j
    #print(k)
    return i-1
    
def swapper(array, p1, p2):
    
    temp = array[p1]  #set one element equal a temp variable
    array[p1] = array[p2]
    array[p2] = temp
    
    
l = [4, 80, 70, 23, 9, 60, 68, 27, 66, 78, 12, 40, 52, 
     53, 44, 8, 49, 28, 18, 46, 21, 39, 51, 7, 87, 99, 69, 62, 84,
     6, 79, 67, 14, 98, 83, 0, 96, 5, 82, 10, 26, 48, 3, 2, 15, 92, 
     11, 55, 63, 97, 43, 45, 81, 42, 95, 20, 25, 74, 24, 72, 91,
     35, 86, 19, 75, 58, 71, 47, 76, 59, 64, 93, 17, 50, 56, 
     94, 90, 89, 32, 37, 34, 65, 1, 73, 41, 36, 57, 77, 30, 22, 
     13, 29, 38, 16, 88, 61, 31, 85, 33, 54]

j = quicksort(vec,0,len(vec),0)
#j = quicksort(l,0,len(l),0)
print(j)

    
