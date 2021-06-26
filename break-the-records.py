#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here

    max_score = scores[0]
    min_score = scores[0]
    highest_count = 0
    lowest_count = 0

    for score in scores[1:len(scores)]:
        if score > max_score:
            highest_count += 1
            max_score = score
        elif score < min_score:
            lowest_count += 1
            min_score = score

    print(highest_count, end=" ")
    print(lowest_count)

if __name__ == '__main__':

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

