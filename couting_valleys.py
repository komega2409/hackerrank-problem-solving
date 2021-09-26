#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    count = 0
    count_arr = []
    valleys = 0
    for step in path:
        if step == 'U':
            count += 1
            count_arr.append(count)
        else:
            count -= 1
            count_arr.append(count)
    print(count_arr)
    for c in range(steps):
        if count_arr[c] == 0 and count_arr[c-1] < 0:
            valleys += 1
    return valleys  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
