valid = []

try:
    with open('sales.txt', 'r') as file:
        sale = file.readline()
        while sale:
            try: 
                valid.append(int(sale))
            except:
                pass
            sale = file.readline()
except:
    print('file doesn\'t found')

print(sum(valid))