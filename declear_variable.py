# name = 'waliullah'
# print('my name is ', name)

# name = input("Enter your name: ")
# print("My name is ", name)

# a = 15
# b = 12
# a = int(input("Enter a number: "))
# b = int(input("Enter b number: "))
a = float(input("Enter a number: "))
b = float(input("Enter b number: "))
summation = a + b
subtraction = a - b
multiplication = a * b
division = a / b
modulus = a % b
floor = a // b
print("The total summation is %s + %s = %.2f" % (a, b, summation))
print("The total subtraction is %s - %s = %.2f" % (a, b, subtraction))
print("The total multiplication is %s * %s = %.2f" % (a, b, multiplication))
print("The total division is %s / %s = %.2f" % (a, b, division))
print("The total modulus is %s %% %s = %.2f" % (a, b, modulus))
print("The total floor is %s // %s = %.2f" % (a, b, floor))