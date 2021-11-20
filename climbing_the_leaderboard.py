#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from bisect import bisect_left
#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # this code gives us the correct result but bad performance
    # player_rank = []
    # for i in range(len(player)):
    #     ranked.append(player[i])
    #     ranked_sorted = sorted(set(ranked), reverse=True)
    #     player_rank.append(ranked_sorted.index(player[i]) + 1)
    # return player_rank

    # this code is optimized for better performance
    counts = Counter(ranked)
    counts = sorted(counts)
    play_ranks = []
    n = len(counts)
    for a in player:
        i = bisect_left(counts, a)
        if i < n and counts[i] == a:
            play_ranks.append(n - i)
        else:
            play_ranks.append(n + 1 - i)
    return play_ranks

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
