#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    most_freq = 0
    count = 0
    id = 0
    for i in range(1,6):
        for j in arr:
            if i == j:
                count += 1
        if count > most_freq:
            most_freq = count
            id = i
        count = 0
    print(id)
if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
