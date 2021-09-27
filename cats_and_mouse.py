#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    catA_pos = x
    catB_pos = y
    mouseC_pos = z

    A_to_C = abs(catA_pos - mouseC_pos)
    B_to_C = abs(catB_pos - mouseC_pos)

    if A_to_C > B_to_C:
        return 'Cat B'
    elif A_to_C < B_to_C:
        return 'Cat A'
    else:
        return 'Mouse C'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
