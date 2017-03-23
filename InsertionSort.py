#!/bin/python3
'''
Author: Sai Uday Bhaskar Mudivarthy
Program: Insertion Sort
Time Complexity: O(n*n)
Best Case: O(n)
Worst Case, Average Case: O(n*n)
'''
import sys
from array import *
def illustrateSortItteration(intarray,i,j):
    for k in range(i+1):
        if k == j:
            print("X",end=" ")
        else:
            print(intarray[k],end=" ")
    print()
    
def printSortedUnsortedSubsets(intarray,i):
    print()
    print("Sorted Subset",end=": ")
    for k in range(i):
        print(intarray[k],end=" ")
    print(end="& Unsorted Subset: ")
    for k in range(i,len(intarray)):
        print(intarray[k],end=" ")
    print()
    print("Finding the perfect position for "+str(x)+" in Sorted Array. We will insert "+str(x)+" inplace of X")

n =  input().strip().split(' ')
intarray = array('i',list(map(int,n)))
isMoved = False
print("Insertion Sort works this way with every itteration by making two subsets Sorted and Unsorted")
for i in range(1,len(intarray)):
    x=intarray[i]
    j= i-1
    printSortedUnsortedSubsets(intarray,i)
    while j>=0 and intarray[j]>x:
        isMoved = True
        illustrateSortItteration(intarray,i,j)
        intarray[j+1]=intarray[j]
        j = j-1
    intarray[j+1] = x
    if not isMoved:
        print("The element "+str(x)+" will be in the right position for the Sorted Array")
        isMoved = False

print()
print("Finally Sorted List: ",end=" ")
for i in intarray:
    print(i,end=" ")
print()
    