# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def isprime(n):
    if n <= 1:
        return False
    
    sqrt_n = math.sqrt(n)
    if sqrt_n .is_integer():
        return False
    
    for i in range(2, int(sqrt_n) +1):
        if n % i == 0:
            return False 
    return True
   
num_test_cases = int(input())   
for i in range(num_test_cases):
    n = int(input())    
    if isprime(n):
         print("Prime")         
    else:
        print("Not prime"))
