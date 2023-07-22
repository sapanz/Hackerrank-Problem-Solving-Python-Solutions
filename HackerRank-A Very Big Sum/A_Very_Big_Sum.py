#!/bin/python3

# Import necessary modules
import math
import os
import random
import re
import sys

# Define a function called 'aVeryBigSum' that takes a list 'ar' as input and returns the sum of its elements
def aVeryBigSum(ar):
    sum = 0  # Initialize a variable 'sum' to store the total sum of elements in the list
    for i in range(len(ar)):  # Loop through each element in the list using its index
        sum += ar[i]  # Add the current element to the running sum
    return sum  # Return the final sum after the loop finishes

if __name__ == '__main__':
    # Open a file for writing the output. The file path is specified in the 'OUTPUT_PATH' environment variable.
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the number of elements in the array from the user input and store it in 'ar_count'
    ar_count = int(input())

    # Read the elements of the array from the user input, split the input by whitespace, and convert each element to an integer.
    # Create a list 'ar' containing these integers.
    ar = list(map(int, input().rstrip().split()))

    # Call the 'aVeryBigSum' function with the 'ar' list as input, and store the result in 'result'
    result = aVeryBigSum(ar)

    # Write the result to the output file and append a newline character at the end.
    fptr.write(str(result) + '\n')

    # Close the output file.
    fptr.close()
