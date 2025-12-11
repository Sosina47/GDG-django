def get_grade(student_grades, student_name):
    try:
        return student_grades[student_name]
    except:
        return 'student not found in the system'

student_grades = {'sosina': 'C', 'sara': 'B', 'Anket': 'A'}
print(get_grade(student_grades, 'sosina'))