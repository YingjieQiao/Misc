#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'minimumSwaps' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY popularity as parameter.
#

def minimumSwaps(popularity):
    length = len(popularity)
    positions = [*enumerate(popularity)]
    positions.sort(key=lambda x:x[1], reverse=True)
    visited = {i:False for i in range(length)}
    count = 0

    for i in range(length):
        if visited[i] or positions[i][0] == i:
            continue
        j = i
        swap = 0
        while not visited[j]:
            visited[j] = True #visited
            j = positions[j][0] #swap
            swap += 1
        if swap > 0:
            count += swap-1 #minus off 1 repeat
    return count


if __name__ == '__main__':