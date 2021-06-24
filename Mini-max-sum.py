#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    min_sum = 0
    max_sum = 0
    arr.sort()
    for i in range(0,4):
        min_sum += arr[i]
    arr.reverse()
    for j in range(0,4):
        max_sum += arr[j]
    print(min_sum, end=" ")
    print(max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
