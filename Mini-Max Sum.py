import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    x = sum(arr)
    
    minValue = x - min(arr)
    maxValue = x - max(arr)
    print(maxValue, minValue)
        
       
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)


