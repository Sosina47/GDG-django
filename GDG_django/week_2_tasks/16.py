def key_to_value(grades):
    output = {}
    vals = grades.values()
    for i in vals:
        if i not in output: 
            output[i] = [name for name in grades.keys() if grades[name] == i]

    return output


grades = {'john': 'A', 'sara': 'B', 'musa': 'A'}
print(key_to_value(grades))