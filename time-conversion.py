#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    d_or_n = s[8:10]
    if d_or_n == "AM":
        if s[0:2] == "12":
            print("00"+s[2:8])
        else:
            print(s[0:8])
    elif d_or_n == "PM":
        converted_hour = int(s[0:2])
        time_24 = converted_hour + 12
        if s[0:2] == "12":
            print("12"+s[2:8])
        else:
            print(str(time_24)+s[2:8])
if __name__ == '__main__':

    s = input()

    timeConversion(s)
