#!/bin/python3
'''
Author: Sai Uday Bhaskar Mudivarthy
Program: Selection Sort
Time Complexity: O(n*n)
'''

import sys
from array import *

def swap(intarray,i,imin):
    temp = intarray[i]
    intarray[i]=intarray[imin]
    intarray[imin]=temp


n =  input().strip().split(' ')
intarray = array('i',list(map(int,n)))
x = 0
for i in range(len(intarray)-1):
    iMin = i
    for j in range(i+1,len(intarray)):
        if intarray[j]<intarray[iMin]:
            iMin = j
    swap(intarray,i,iMin)

for i in intarray:
    print(i)


