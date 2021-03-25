#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    
    patteren = r"@gmail\.com$"
    regex = re.compile(patteren)
    
    firstNamesList = []
        

    for N_itr in range(N):
        firstNameEmailID = input().split()
        
        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        
        if regex.search(emailID):
            firstNamesList.append(firstName)
            
    firstNamesList.sort()
    
    for name in firstNamesList:
        print(name)

