n = [1, -2, -3,-4]
sum = 0
mul = -1
for i in range(len(n)):
    sum+=n[i]
print(sum)
if sum < 0:
    summation = sum*mul
    print(summation)
else:
    print(sum)