#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a.sort()
    subarr = []
    temp_arr = []
    int1 = 0

    for i in range(len(a)):
        if not temp_arr:
            temp_arr.append(a[i])
        


if __name__ == '__main__':
    fptr = open('test_cases.txt', 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
