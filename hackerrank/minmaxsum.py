import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def qsort(array):
    less = []
    equal = []
    greater = []
                                    # source arr = [12, 4, 5, 6, 7, 3, 1, 15]
    if len(array) > 1:
        pivot = array[0]            # p = 12                    # p = 4
        for x in array:
            if x < pivot:
                less.append(x)      # [4, 5, 6, 7, 3, 1]        # [3, 1]
            if x == pivot:
                equal.append(x)     # [12]                      # [4]
            if x > pivot:
                greater.append(x)   # [15]                      # [5, 6, 7]

        return qsort(less) + equal + qsort(greater)
    else:
        return array

def miniMaxSum(arr):
    s_array = qsort(arr)
    max_sum = sum(s_array[1:])
    min_sum = sum(s_array[0:-1])
    print("%d %d" % (min_sum, max_sum))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)