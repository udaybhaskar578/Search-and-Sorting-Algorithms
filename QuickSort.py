#!/bin/python3
'''
Author: Sai Uday Bhaskar Mudivarthy
Program: Quick Sort
Time Complexity: O(n log n)
Worst Case: O(n*n)
'''

import sys
from array import *

def Swap(A,i,j):
    temp = A[i]
    A[i]=A[j]
    A[j]=temp

def QuickSort(A,start,end):
    if start<end:
        pIndex = PartitionIndex(A,start,end)
        QuickSort(A,start,pIndex-1)
        QuickSort(A,pIndex+1,end)

def PartitionIndex(A,start,end):
    pivot = A[end]
    pIndex = start
    for i in range(start,end):
        if(A[i] <= pivot):
            Swap(A,i,pIndex)
            pIndex = pIndex +1
    Swap(A,pIndex,end)
    return pIndex

n =  input().strip().split(' ')
intarray = array('i',list(map(int,n)))
QuickSort(intarray,0,len(intarray)-1)
print()
print("Sorted List Follows")
for i in intarray:
    print(i,end=" ")
print()

