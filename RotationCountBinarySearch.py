#!/bin/python3
'''
Author: Sai Uday Bhaskar Mudivarty
Program: Find number of rotations occured on a sorted array
Pre Req: The sorted array must not contain any duplicate elements
'''
def FindRotationCount(A,n):
    start = 0
    end = n-1
    isValid = True
    while(start<=end):
        if A[start] <= A[end]:
            return start
        mid = start + int((end-start)/2)
        nextToMid = (mid+1)%n
        prevToMid = (mid-1)%n
        if A[mid]<=A[nextToMid] and A[mid] <=A[prevToMid]:
            return mid
        elif A[mid]<=A[end]:
            end = mid-1
        elif A[mid]>=A[start]:
            start = mid+1
        else:
            break
    return -1

array = list(map(int,input("Please enter a sorted array which could have been rotated towards right: ").strip().split(' ')))
count = FindRotationCount(array,len(array))
if count>-1:
    print("The array has been rotated "+str(count)+" times :)")
else:
    print("Improper data")

