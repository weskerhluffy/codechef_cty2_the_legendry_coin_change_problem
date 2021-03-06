#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
'''
Created on 25 dic 2019

@author: ernestoalvarado
'''
# XXX: https://www.codechef.com/problems/CTY2

import math
import os
import random
import re
import sys

import fileinput
#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#


def getWays(n, c):
    dp = []
    c_len = len(c)
    dp.append([1] * (c_len + 1))
    for _ in range(n):
        dp.append([0] * (c_len + 1))
    
    for i in range(1, n + 1):
        for j in range(1, c_len + 1):
            dpt = dp[i][j - 1]
            cn = c[j - 1]
            if cn <= i:
                dpt += dp[i - cn][j]
            dp[i][j] = dpt
    return dp[n][-1]


if __name__ == '__main__':

    n, _ = [int(x) for x in input().strip().split()]
    c = [int(x) for x in input().strip().split()]

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'
    # XXX: https://stackoverflow.com/questions/1450393/how-do-you-read-from-stdin
    ways = getWays(n, c)
    
    print(str(ways))
