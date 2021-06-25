#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    final_grades = []
    for grade in grades:
        for i in range(0,106):
            if 38 <= grade < i and i % 5 == 0:
                if i - grade < 3:
                    grade = i
                    final_grades.append(grade)
                    break
                else:
                    final_grades.append(grade)
                    break
            elif grade < 38:
                final_grades.append(grade)
                break

    for i in final_grades:
        print(i)



if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    gradingStudents(grades)
