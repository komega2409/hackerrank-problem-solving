#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    pair = 0
    pairs = []
    colors = set()
    
    for i in ar:
        colors.add(i)
    
    for i in colors:
        count = 0
        for j in ar:
            if i == j:
                count += 1
        pairs.append(count)

    for i in pairs:
        if i > 1:
            pair += math.floor(i/2)
    return pair
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
