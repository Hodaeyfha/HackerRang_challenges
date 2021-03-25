def multiplication_table():

    multiplcation = int(input('enter number 1: '))
    table = int(input('enter number 2:'))
    for i in range(multiplcation, table +1):

        for j in range(1 , 11):

            print(i, "X", j, "=", i*j)
        print('-----------------')
        
multiplication_table()
