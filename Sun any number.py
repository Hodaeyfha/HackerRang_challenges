
def Sum_any_number():

    print("This game will take severel number and print the avarage of them")

    count = int(input("How many number would you like to sum: "))

    current_count = 0
    sum = 0

    while current_count < count:
        number = float(input("Enter a number: "))
        sum  += number
        current_count +=1

    print("Sum of all numbers = ", sum)
    print("Avarage of all numbers = ", sum/number)


Sum_any_number()
