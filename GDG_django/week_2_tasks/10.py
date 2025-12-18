x = int(input('enter a number: '))
rev = 0
temp = x
while temp > 0:
    rev *= 10
    rev += temp % 10
    temp //= 10
print(rev == x)