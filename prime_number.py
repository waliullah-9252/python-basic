num = int(input('Enter a number: '))
flag = 0
for i in range(2, num):
    if num % i == 0:
        flag = 1
        break
if flag == 0 and num > 1:
    print(num,' is prime')
else:
    print(num,' is not prime')