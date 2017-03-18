#!/bin/python3
'''
Author: Sai Uday Bhaskar Mudivarthy
Program: Insertion Sort
Time Complexity: O(n*n)
'''
import sys
from array import *


n =  input().strip().split(' ')
intarray = array('i',list(map(int,n)))
isMoved = False
print()
print("Insertion Sort works this way with every itteration")
for i in range(1,len(intarray)):
    x=intarray[i]
    j= i-1
    print()
    print("Sorted Array",end=": ")
    for k in range(i):
        print(intarray[k],end=" ")
    print(end="& Unsorted Array: ")
    for k in range(i,len(intarray)):
        print(intarray[k],end=" ")
    print()
    print("Finding the perfect position for "+str(x)+" in Sorted Array. We will insert "+str(x)+" inplace of X")
    while j>=0 and intarray[j]>x:
        isMoved = True
        intarray[j+1]=intarray[j]
        
        for k in range(i+1):
            if k == j:
                print("X",end=" ")
            else:
                print(intarray[k],end=" ")
        j = j-1
        print()
    intarray[j+1] = x
    if not isMoved:
        print("The element "+str(x)+" will be in the right position for the Sorted Array")
        print()
        isMoved = False

print()
print("Sorted List Follows")
for i in intarray:
    print(i,end=" ")
print()
    