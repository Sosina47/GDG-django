file_name = input('enter file name: ')

try:
    with open(file_name , 'r') as file:
        text = file.read()
        print(text.upper())
except:
    print('file not found')
