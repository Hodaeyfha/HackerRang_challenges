'''

Count Vowels
– Enter a string and the program counts the number of vowels in the text.
For added complexity have it report a sum of each vowel found.
'''

string_caracters = input('Enter caracter: ')
count = 0
for i in string_caracters:
    
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        count = count +1

print("Number of vowels are:", count)

    
    

