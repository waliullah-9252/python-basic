# use built in functions
# character = input('Enter a character: ')
# if character.islower():
#     print(character," is lower case")
# elif character.isupper():
#     print(character," is upper case")
# else:
#     print(character,' is not a valid character')


# lower case and upper case character check program
ch = input('Enter a character: ')
if ch >= 'a' and ch <= 'z':
    print(ch,' is a lower case character')
elif ch >= 'A' and ch <= 'Z':
    print(ch,' is a upper case character')
else:
    print(ch,' is not a character')