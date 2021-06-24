#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    # Write your code here
    above_area = H*W
    beneath_area = H*W
    front_area = 0
    behind_area = 0
    left_area = 0
    right_area = 0
    rest_area = 0
    total = 0
    for i in range(0, W):
        front_area += A[0][i]

    for j in range(0, W):
        behind_area += A[H-1][j]

    for x in range(0, H):
        left_area += A[x][0]

    for y in range(0, H):
        right_area += A[y][W-1]

    for i in range(H):
        for j in range(W):
            if j != W-1:
                rest_area += abs(A[i][j] - A[i][j+1])
            if i != H-1:
                rest_area += abs(A[i][j] - A[i+1][j])

    total = front_area + behind_area + left_area + right_area + above_area + beneath_area + rest_area
    print(total)
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    surfaceArea(A)
