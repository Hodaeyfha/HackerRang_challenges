'''Enter a string and the program will reverse it and print it out.'''
def reverse_stringe(l):

    rever = ' '
    for i in l:
        rever = i + rever

    return rever

input_str = 'margorp'

if __name__ == '__main__':
    print('Reverse string using for loop = ', reverse_stringe(input_str))


reverse_stringe(input_str)
    


