
def palindrom():
    #here we exprirence
    try:
         case_user = input("Enter your string: ")           #we requested the user andre[eat on the required
         string = ' '
         for i in case_user:
              string = i + string
    # print required
         print('String in reversd order : ', '[ ', case_user,' ]')
    #check if the introduction is similar or   
         if case_user in string:
             print("This is a Palindrome String")          
         else:
             print("This is Not a Palindrome String")
    #check if the error is printed   
    except ValueError:
       print('He got a mistake of the entry again')


g = palindrom()
    




























