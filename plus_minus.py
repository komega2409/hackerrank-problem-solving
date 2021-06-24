#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos_count = 0
    neg_count = 0
    minus_count = 0
    for i in range(0,len(arr)):
        if arr[i] > 0:
            pos_count += 1
        elif arr[i] < 0:
            neg_count += 1
        else:
            minus_count += 1
    print("{:.6}".format(pos_count/n))
    print("{:.6}".format(neg_count/n))
    print("{:.6}".format(minus_count/n))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
