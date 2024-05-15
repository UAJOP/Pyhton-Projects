students = ["Kaan", "Efe", "Baran", "Ayberk", "Esma"]
students_no = ["Kaan", "Efe"]

last_students = [student.upper() if student in students_no else student.lower() for student in students]

print(last_students)
