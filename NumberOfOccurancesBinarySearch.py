#!/bin/python3
'''
Author: Sai Uday Bhaskar Mudivarthy
Program: Number of occurances of an element in an array using binary seach
Time Complexity: O(Log n)
'''
'''
BinarySearch(Array,lengthOfArray,elementToBeFound,firstOrLast)
firstOrLast = 0 makes the program to look for the first occurance
firstOrLast = 1 makes the program to look for the last occurance
'''
def BinarySearch(A,n,x,fl):
    start = 0
    end = n-1
    result = -1
    while(start<=end):
        mid = start + int((end-start)/2)
        if A[mid]==x:
            result = mid
            if fl == 0:
                end = mid-1
            else:
                start = mid+1
        elif A[mid] > x:
            end = mid-1
        else:
            start = mid+1
    return result

array = list(map(int,input("Please enter the values of an array in a sorted order(ASC): ").strip().split(' ')))
x= int(input("Enter the value to be found: "))
lengthArray = len(array)
firstOccurance = BinarySearch(array,lengthArray,x,0)
lastOccurance = BinarySearch(array,lengthArray,x,1)
totalOccurances = lastOccurance -firstOccurance +1

if(firstOccurance > 0 and lastOccurance >0):
    print("Hurray !!! Number of occurances of the element is " + str(totalOccurances) + " times :) ")
else:
    print("We haven't found the element in the given array :(")
