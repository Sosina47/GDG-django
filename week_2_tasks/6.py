valid = []

with open('sales.txt', 'r') as file:
    sale = file.readline()
    while sale:
        try: 
            valid.append(int(sale))
        except:
            pass
        sale = file.readline()

print(sum(valid))