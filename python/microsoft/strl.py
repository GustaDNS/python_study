str = 'That is a string because phrase is included by simple aspas'
int = 4 # this is a integer
print(str, int)
str1 = str + ' Concatenation between 2 strings'
print(str1)
# we can add a string and a intenger? let's test
#num = 2
#string1 = 'first try'
#conc = num + string1
#print(conc)
#it's impossible to add a str and int, two differents operand types


sentence = 'The name of my dog is Koko'
print(sentence.upper()) #all char in the string UPPER 
print(sentence.lower()) #all char in the string is lower
print(sentence.capitalize()) #the first letter of the string become a upper letter
print(sentence.count('o'))#count how many 'a' are in the string (ex: Gustavo -> has 1 'a')


first_name = input('What is your name? ')
last_name = input('What is your last name? ')
print ('Hello', first_name.capitalize() + ' ' + last_name.capitalize()) 
#capitalize() in Python is used to convert the first character of a string to uppercase 
#and the remaining characters to lowercase.

