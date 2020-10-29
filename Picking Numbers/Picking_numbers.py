#!/bin/python

import math
import os
import random
import re
import sys

# Complete the pickingNumbers function below.
def pickingNumbers(a):
 count = [0 for i in xrange(101)]
 for i in a:
    count[i] += 1
 ans = 0
 for i in xrange(0, 100):
    ans = max(ans, count[i] + count[i + 1])
 return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input().strip())

    a = map(int, raw_input().rstrip().split())

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
