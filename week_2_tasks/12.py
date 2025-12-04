valid = []

with open('numbers.txt', 'r') as file:
    number = file.readline()
    while number:
        try:
            valid.append(int(number))
        except:
            pass
        number = file.readline()

print(sum(valid))