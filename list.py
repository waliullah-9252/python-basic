lst = [2, 3, 4, 5, 6, 7, 8, 9]
# del lst[0]
# lst.append(10)
print(lst[::])
print(len(lst))
sum = 0
for i in range(len(lst)):
    sum += lst[i]
print(sum)