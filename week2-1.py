# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 11:00:46 2016

@author: kalpoffer
"""

#load content 1

my_file = open("/home/kalpoffer/Downloads/intar.txt").read()
vec = []
for e in my_file.split("\n"):
    vec.append(e.strip("\r"))
    
#created the vector which contains all the integers from the file

#if i remember well, we use an index k to find a random element into the array
#to which create a pivot kind of structure used to the partition of the array


"""
the quicksort which sorts using the last element of the array as a pivot
"""

#####################

def quicksort_l(array, left, right,c):
    
    
    if(len(array[left:right]) != 0):
        c.append(len(array[left:right])-1) 
    
    if(left >= right):
        return 
    
    pivot = partition_l(array, left, right)
    
    #print("just the pivot: " + str(pivot))
    #print(array[left:pivot])
    quicksort_l(array, left, pivot,c)
    quicksort_l(array, pivot+1, right,c)
    
    return (array,c)
    
# i want to try a different kind of partition. I can use the same logic as the
#previous one, but using the last element as pivot.

"""
def partition_l(array, left, right):
    
    piv_item = int(array[right-1]) 
    #we set the pivot as the first element in the array
    
    i = left
    j = left#we set 2 pointers pointing at the same 
    #element of the given array
    
    while(j < right):
        if(int(array[j]) < piv_item): #assuming there're no elements equal all around
            swapper(array, j, i)
            i=i+1
        print array
        j=j+1
        
    swapper(array, right-1, i)
    
    print(piv_item)
    print array
    return (i)
"""

"""
def partition_l(array,left,right):
    
    piv_item = int(array[right-1])

    i = right-2
    j = right-2
    
    while(j >= left):
        
        if(int(array[j]) > piv_item):
            swapper(array,j,i)
            i=i-1
        j=j-1
    
    swapper(array,right-1,i+1)
    return(i+1)
"""

def partition_l(array, left, right):
    
    
    swapper(array, left, right-1)
    
    piv_item = int(array[left]) #we set the pivot as the first element in the array
    
    
    i = left+1
    j = left+1 
    #we set 2 pointers pointing at the same 
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

#####################

"""
the quicksort which sorts using the first element of the array as a pivot
"""

#####################

def quicksort_f(array, left, right,c):
    
    #print("printing c: " + str(c))
    
    if(len(array[left:right]) != 0):
        c.append(len(array[left:right])-1) 
    
    
    if(left >= right):
        #print("with the return: " + str(c))
        return 
    
    pivot = partition_f(array, left, right)
    #c = c + len(array[left:pivot])
    quicksort_f(array, left, pivot,c)
    #print("here")
    #c = c + len(array[pivot+1:right])
    quicksort_f(array, pivot+1, right,c)

    return (c)

def partition_f(array, left, right):
    
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

#####################

"""
the quicksort which sorts using the middle element of the array as a pivot
"""

#####################

def quicksort_m(array, left, right,c):
    
    
    if(len(array[left:right]) != 0):
        c.append(len(array[left:right])-1) 
    
    
    if(left >= right):
        return 
    
    pivot = partition_m(array, left, right)
    #c = c + len(array[left:pivot])
    quicksort_m(array, left, pivot,c)
    #print("here")
    #c = c + len(array[pivot+1:right])
    quicksort_m(array, pivot+1, right,c)

    return (array,c)



def partition_m(array, left, right):
    
    #the set of the elements used into the median finding
    
    #print(array)
    
    
    f=int(array[left])
    l=int(array[right-1])
    m=int(array[int((left+(right-1))/2)])
    
    k =[f,l,m]
    k.sort()
    
    #print(k[1])
    swapper(array,array.index(str(k[1])),left)
    #print("after swap: " + str(array))
    piv_item = int(array[left]) #we set the pivot as the first element in the array
    
    
    #print("array: " + str(array))
    
    #print("left and right: " + str(left) + "," + str(right))
    i = left+1
    j = left+1#we set 2 pointers pointing at the same 
    #element of the given array
    
    #print("swap between 2 elements: " + str(med) + " the pivot and the first element " + str(left))
    
    #print("here we can use the same logic as the first partition")
    
    
    # print("array swapper" + str(array))
    
    while(j < right):
        if(int(array[j]) < piv_item): #assuming there're no elements equal all around
            swapper(array, j, i)
            i=i+1
        
        j=j+1
        
    swapper(array, left, i-1)
    return (i-1)


#####################

"""
Helper Functions
"""

#####################

def swapper(array, p1, p2):
    
    temp = array[p1]  #set one element equal a temp variable
    array[p1] = array[p2]
    array[p2] = temp
    



######################

#content used for tests from files


my_file = open("/home/kalpoffer/Downloads/number.txt").read()
vec2 = []
for e in my_file.split("\n"):
    vec2.append(e.strip("\r"))



"""
my_file = open("/home/kalpoffer/Downloads/numpy.txt").read()
vec2 = []
for e in my_file.split("\n"):
    vec2.append(e.strip("\r"))
"""

l = [3,9,8,4,6,10,2,1,7,5]


o = [8, 2, 4, 5, 7, 1]
#print(vec2)
#j = quicksort_f(vec,0,len(vec),[])

j = quicksort_f(l,0,len(l),[])
#j = quicksort_l(vec,0,len(vec),[])
print(j)
