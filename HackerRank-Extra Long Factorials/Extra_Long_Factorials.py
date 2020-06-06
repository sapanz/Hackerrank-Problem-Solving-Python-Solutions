#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    if n == 1:
        return 1
    return n * extraLongFactorials(n-1)

if __name__ == '__main__':
    print(extraLongFactorials(int(input())))
