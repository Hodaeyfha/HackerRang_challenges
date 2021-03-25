def fibonacci(n):
    # return a list of fibonacci numbers
     lis = [0,1]
     for i in range(2,n):
         lis.append(lis[i-2] + lis[i-1])
     return(lis[0:n])
    '''a = 0
    b = 1
    l = []
    
    if n == 0:
        pass
    elif n == 1:
        l.append(n)
    else:
        l.append(a)
        l.append(b)
        
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            l.append(c)
    return l
    '''
#complete the lambda function
cube = lambda x : x ** 3

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
