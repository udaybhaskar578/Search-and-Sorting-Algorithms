#!/bin/python3
'''
Author: Sai Uday Bhaskar Mudivarty
Program: Find number in a sorted array rotated towards the right
Pre Req: The sorted array must not contain any duplicate elements
'''
def CircularArraySearch(A,n,x):
    start = 0
    end = n-1
    isValid = True
    while(start<=end):
        mid = start + int((end-start)/2)
        if A[mid] == x:
            return mid
        elif A[mid]< A[end]:
            if A[mid]<x and A[end]>=x:
                start=mid+1
            else:
                end = mid-1
        elif A[mid]>=A[start]:
            if A[start]<=x and A[mid]>x:
                end = mid-1
            else:
                start = mid+1
    return -1

array = list(map(int,input("Please enter a sorted array which could have been rotated towards right: ").strip().split(' ')))
x=int(input("Enter the number you are searching for: "))
result = CircularArraySearch(array,len(array),x)
if(result > -1):
    print("Hurray !!! We found the elment in that array :) ")
else:
    print("We haven't found the element in the given array :(")


