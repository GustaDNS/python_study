nbr1 = 12
nbr2 = 7

print(nbr1 + nbr2)
print(nbr1 - nbr2)
print(nbr1 * nbr2)
print(nbr1 / nbr2)
print(nbr1 ** nbr2)
print(nbr1 % nbr2) #modulo

feb = 28
print(str(feb) + ' days in February')
#why str(feb) and not feb?
#because we can + a integer with string, so we need to
#"convert" the integer to string, using the fucntion "str()"
#then my 28 (integer) is converted to 28 (string)

first_num = input('Please enter a number: ')
second_num = input('Please enter another number: ')
print(int(first_num) + int(second_num))
#print(float(first_num) + float(second_num))