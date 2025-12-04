scores = {'john': 85, 'sara': 92, 'fraol': 78}
name = input('enter student\'s name: ')

try:
    print(scores[name.lower()])
except:
    print('student not found!')