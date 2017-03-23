#!/bin/python3
'''
Author: Sai Uday Bhaskar Mudivarthy
Program: Number of occurances of an element in an array using binary seach
Time Complexity: O(Log n)
'''
'''
BinarySearch(Array,lengthOfArray,elementToBeFound)
'''
def BinarySearch(A,n,x):
    start = 0
    end = n-1
    result = -1
    while(start<=end):
        mid = start + int((end-start)/2)
        if A[mid]==x:
            result = mid
            end = mid-1
        elif A[mid] > x:
            end = mid-1
        else:
            start = mid+1
    return result

array = list(map(int,input("Please enter the values of an array in a sorted order(ASC): ").strip().split(' ')))
x= int(input("Enter the value to be found: "))
y = int(input("Which occurance of that given element are you looking for: "))
lengthArray = len(array)
firstOccurance = BinarySearch(array,lengthArray,x)
nthoccurance = firstOccurance + y -1


if(array[nthoccurance]==x):
    print("Hurray !!! The given Nth occurance of the given value happens at "+str(nthoccurance)+" :)")
elif firstOccurance > -1:
    print("The given element is found in the array, but there are no "+str(y)+" occurances of that element")
else:
    print("We haven't found the element in the given array :(")
