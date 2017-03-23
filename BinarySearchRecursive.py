#!/bin/python3
'''
Author: Sai Uday Bhaskar Mudivarthy
Program: Binary Search Iterative
Time Complexity: O(Log n)
'''
def BinarySearch(A,start,end,x):
    if(start >end):
        return -1
    mid = start + int((end-start)/2)
    if A[mid]==x:
        return mid
    elif A[mid] > x:
        return BinarySearch(A,start,mid-1,x)
    else:
        return BinarySearch(A,mid+1,end,x)


array = list(map(int,input("Please enter the values of an array in a sorted order(ASC): ").strip().split(' ')))
x= int(input("Enter the value to be found: "))
result = BinarySearch(array,0,len(array)-1,x)
if(result > -1):
    print("Hurray !!! We found the elment in that array :) ")
else:
    print("We haven't found the element in the given array :(")
