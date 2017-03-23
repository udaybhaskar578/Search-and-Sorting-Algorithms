#!/bin/python3
'''
Author: Sai Uday Bhaskar Mudivarthy
Program: Binary Search Iterative
Time Complexity: O(Log n)
'''
def BinarySearch(A,n,x):
    start = 0
    end = n-1
    while(start<=end):
        mid = start + int((end-start)/2)
        if A[mid]==x:
            return mid
        elif A[mid] > x:
            end = mid-1
        else:
            start = mid+1
    return -1

array = list(map(int,input("Please enter the values of an array in a sorted order(ASC): ").strip().split(' ')))
x= int(input("Enter the value to be found: "))
result = BinarySearch(array,len(array),x)
if(result > -1):
    print("Hurray !!! We found the elment in that array :) ")
else:
    print("We haven't found the element in the given array :(")
