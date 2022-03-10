import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    neg = 0
    pos = 0
    nullv = 0
    for a in arr:
        if a > 0:
            pos += 1
        elif a < 0:
            neg += 1
        else:
            nullv += 1
            
    print('{0:.6f}'.format(pos/len(arr)))
    print('{0:.6f}'.format(neg/len(arr)))
    print('{0:.6f}'.format(nullv/len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
