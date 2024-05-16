student_dict = {
    'name': 'Md. Sayem Uddin',
    'ID': 'C201127',
    'grades': {'C++': 'A+', 'DLD': 'B-', 'Math 2': 'A+'}
}

# Printing the student dictionary
print("Initial Student Dictionary:")
print(student_dict)

# Adding a new subject and its grade
student_dict['grades']['English'] = 'B'

# Updating the grade for DLD
student_dict['grades']['DLD'] = 'B'

# Removing the 'Math 2' grade
removed_grade = student_dict['grades'].pop('Math 2')

# Printing the modified dictionary
print("\nModified Student Dictionary:")
print(student_dict)
print("Removed Grade:", removed_grade)




# Dictionary where keys are student names and values are lists of grades
student_grades = {
    'Ifty': ['A+', 'B-', 'A+'],
    'Afif': ['B', 'B', 'C+'],
    'Ismail': ['A', 'A-', 'B']
}

# Calculate the average grade for each student
average_grades = {}
for student, grades in student_grades.items():
    # Converting grades to numerical values for easier calculation
    numerical_grades = [4 if grade == 'A+' else 3.7 if grade == 'A' else 3.3 if grade == 'A-' else 
                        3 if grade == 'B+' else 2.7 if grade == 'B' else 2.3 if grade == 'B-' else 
                        2 if grade == 'C+' else 1.7 if grade == 'C' else 1.3 if grade == 'C-' else 
                        1 if grade == 'D+' else 0 for grade in grades]
    average_grade = sum(numerical_grades) / len(numerical_grades)
    average_grades[student] = average_grade

# Printing the average grades for each student
print("Average grades for each student:")
for student, avg_grade in average_grades.items():
    print(f"{student}: {avg_grade}")
