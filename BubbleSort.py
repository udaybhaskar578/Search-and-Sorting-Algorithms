#!/bin/python3
'''
Author: Sai Uday Bhaskar Mudivarthy
Program: Bubble Sort
Time Complexity: O(n*n)
Best Case: O(n)
Worst Case, Average Case: O(n*n)
'''

import sys
from array import *

def swap(intarray,i,imin):
    temp = intarray[i]
    intarray[i]=intarray[imin]
    intarray[imin]=temp


n =  input().strip().split(' ')
intarray = array('i',list(map(int,n)))
for i in range(1,len(intarray)):
    isSwapped = False
    print("Iteration: " + str(i))
    for j in range(len(intarray)-1):
        if intarray[j] > intarray[j+1]:
            isSwapped = True
            swap(intarray,j,j+1)
    for k in intarray:
        print(k,end=",")
    print()
    if not isSwapped:
        break

for i in intarray:
    print(i,end=",")
    

