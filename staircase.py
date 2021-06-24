#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    for i in range(0,n):
        for j in range(0,n-1):
            print(" ",end="")
        for z in range(0,i+1):
            print("#",end="")
        print()
        n = n - 1

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
