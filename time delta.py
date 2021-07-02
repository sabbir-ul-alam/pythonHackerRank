#!/bin/python3

import math
import os
import random
import re
import sys
import datetime
import calendar

# Complete the time_delta function below.
def convertintosec(time):
    sec=0

    return sec
def time_delta(t1, t2):
    res=0
    format="%a %d %b %Y %H:%M:%S %z"
    t1=datetime.datetime.strptime(t1,format)
    t2 = datetime.datetime.strptime(t2, format)
    #print(t1)

    return int(abs((t1-t2).total_seconds()))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)
        print (delta)

        #fptr.write(delta + '\n')

    #fptr.close()
