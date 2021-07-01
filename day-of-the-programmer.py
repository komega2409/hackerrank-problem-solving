#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    if year == 1918:
        print("26.09.%s" %year)
    elif (year <= 1917 and year % 4 == 0) or ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)):
        print("12.09.%s" %year)
    else:
        print("13.09.%s" %year)
if __name__ == '__main__':

    year = int(input().strip())

    result = dayOfProgrammer(year)

