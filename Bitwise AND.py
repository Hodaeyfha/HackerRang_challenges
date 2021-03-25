#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#

def bitwiseAnd(N, K):
    # Write your code here
    
    max_bitwise = 0
    for i in range(1, N+1):
        for j in range(1, i):
            bitwise = i & j
            
            if max_bitwise < bitwise < K:
                max_bitwise = bitwise
                
                if max_bitwise == K -1:
                    return max_bitwise
                
    return max_bitwise

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        N = int(first_multiple_input[0])

        K = int(first_multiple_input[1])

        res = bitwiseAnd(N, K)

        fptr.write(str(res) + '\n')
        print(bitwiseAnd(N, K))  

    fptr.close()

