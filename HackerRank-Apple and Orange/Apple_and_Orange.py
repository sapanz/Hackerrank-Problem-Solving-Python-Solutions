#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Initialize counters for apples and oranges that fall within the house's range [s, t].
    acount = 0
    bcount = 0

    # Iterate through the apples' positions.
    for i in range(len(apples)):
        # Calculate the actual position of the apple relative to the tree a.
        temp = a + apples[i]
        # Check if the apple's position falls within the house's range [s, t].
        if temp in range(s, t + 1):
            # If the apple falls within the house's range, increment the apple counter.
            acount += 1

    # Iterate through the oranges' positions.
    for i in range(len(oranges)):
        # Calculate the actual position of the orange relative to the tree b.
        temp = b + oranges[i]
        # Check if the orange's position falls within the house's range [s, t].
        if temp in range(s, t + 1):
            # If the orange falls within the house's range, increment the orange counter.
            bcount += 1

    # Print the final count of apples and oranges that fall within the house's range.
    print(acount)
    print(bcount)

if __name__ == '__main__':
    # Read the input for the house's range [s, t].
    st = input().split()
    s = int(st[0])
    t = int(st[1])

    # Read the input for the positions of trees a and b.
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])

    # Read the input for the number of apples and oranges.
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])

    # Read the input for the positions of apples and oranges as lists.
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    # Call the countApplesAndOranges function with the given inputs.
    countApplesAndOranges(s, t, a, b, apples, oranges)
