#!/bin/python3
'''
Author: Sai Uday Bhaskar Mudivarthy
Program: Merge Sort
Time Complexity: O(n log n)
'''

import sys
from array import *

def Merge(L,R,A):
    nL = len(L)
    nR = len(R)
    i=0
    j=0
    k=0
    while i<nL and j<nR:
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i+1
        else:
            A[k] = R[j]
            j = j+1
        k = k+1
    while i<nL:
        A[k] = L[i]
        k = k+1
        i = i+1
    while j<nR:
        A[k] = R[j]
        k=k+1
        j=j+1

def MergeSort(A):
    n = len(A)
    if n<2:
        return
    mid = int(n/2)
    left = array('i')
    right = array('i')

    for i in range(mid):
        left.append(A[i])
    for i in range(mid,n):
        right.append(A[i])
    MergeSort(left)
    MergeSort(right)
    Merge(left,right,A)
    
n =  input().strip().split(' ')
intarray = array('i',list(map(int,n)))
MergeSort(intarray)
print()
print("Sorted List Follows")
for i in intarray:
    print(i,end=" ")
print()