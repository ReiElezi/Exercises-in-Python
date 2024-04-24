
total_grades = 0
num_students = 0
grade = float(input("Enter a student's grade (or -1 to stop): "))
while grade != -1:
    total_grades += grade
    num_students += 1
    grade = float(input("Enter a student's grade (or -1 to stop): "))


if num_students > 0:
    average_grade = total_grades / num_students
    print(f"The average of the entered grades is: {average_grade}")
else:
    print("No grades were entered.")

#ora 12 btw