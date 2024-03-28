num = int(input("Enter a number: "))
divisoin = int(num / 10)
divisor = num % 10
print(divisoin, divisor)
if divisoin%divisor == 0 or divisor%divisoin == 0:
    print("yes")
else:
    print("no")