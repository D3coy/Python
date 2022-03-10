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

# may check hour part of time instead, as a var. 2
def timeConversion(s):
    if s[-2:] == "PM":
        if int(s[:2]) < 12:
            hour = int(s[:2]) + 12
        else:
            hour = "12"
        return "{}{}".format(str(hour), s[2:-2])
    
    elif s[-2:] == "AM":
        if int(s[:2]) < 12:
            hour = s[:2]
        else:
            hour = "00"
        return "{}{}".format(str(hour), s[2:-2])
    
    else:
        return "[ERROR] Wrong time format"

if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)