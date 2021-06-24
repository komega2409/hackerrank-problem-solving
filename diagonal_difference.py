#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
# Write your code here

def diagonalDifference(arr):
    l_to_r = 0
    r_to_l = 0
    for i in range(0,len(arr)):
        l_to_r += arr[i][i]
    for j in range(0,len(arr)):
        r_to_l += arr[j][len(arr)-j-1]
    print(abs(l_to_r - r_to_l))


if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
