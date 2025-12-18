def get_grade(student_grades, student_name):
    try:
        return student_grades[student_name]
    except KeyError:
        return 'student not found in the system'
    except:
        return 'something went wrong'

student_grades = {'sosina': 'C', 'sara': 'B', 'Anket': 'A'}
print(get_grade(student_grades, 'sosina'))