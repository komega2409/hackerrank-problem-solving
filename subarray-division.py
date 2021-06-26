#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    sum = 0
    times = 0
    count = 0
    i = 0
    while times <= m and i <= len(s)-1:
        sum += s[i]
        if sum == d and times+1 == m:
            count += 1
            s = s[1:len(s)]
            times = -1
            sum = 0
            i = -1
        if times == m-1:
            s = s[1:len(s)]
            times = -1
            sum = 0
            i = -1
        times += 1
        i += 1
    print(count)
if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)
