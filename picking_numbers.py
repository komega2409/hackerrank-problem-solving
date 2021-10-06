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
    a.append(0)
    subarr = []
    temp_arr = []
    int1 = 0
    max_length = 0

    for i in range(len(a)):
        if not temp_arr:
            temp_arr.append(a[i])
            int1 = temp_arr[0]
        else:
            if a[i] - int1 == 0 or a[i] - int1 == 1:
                temp_arr.append(a[i])
            else:
                subarr.append(temp_arr)
                temp_arr = []
                temp_arr.append(a[i])
                int1 = temp_arr[0]

    for sub in subarr:
        if len(sub) > max_length:
            max_length = len(sub)
    return max_length
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
