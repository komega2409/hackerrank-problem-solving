#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    FIRST_PAGE = 1
    LAST_PAGE = n
    slips_from_first = 0
    slips_from_last = 0
    
    if p % 2 == 0:
        slips_from_first = math.floor((p + FIRST_PAGE) / 2)
        slips_from_last = math.floor((LAST_PAGE - p) / 2)
    else:
        slips_from_first = (p - FIRST_PAGE) / 2
        slips_from_last = math.floor(((LAST_PAGE + 1) - p) / 2)
    
    if (p == FIRST_PAGE) or (p == LAST_PAGE):
        return 0
    elif (slips_from_first > slips_from_last):
        return int(slips_from_last)
    else:
        return int(slips_from_first)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
