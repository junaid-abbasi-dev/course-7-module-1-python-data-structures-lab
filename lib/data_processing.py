# This module contains functions to process student data.
students = [
    (101, "Alice Johnson", "Computer Science"),
    (102, "Bob Smith", "Mathematics"),
    (103, "Charlie Davis", "Physics"),
    (104, "David Wilson", "Computer Science"),
    (105, "Eve Lewis", "Mathematics"),
]

def format_student_data(student):
    formatted_student = f"ID: {student[0]} | Name: {student[1]} | Major: {student[2]}"
    return formatted_student

def display_students(student_list):
    for student in student_list:
        print(format_student_data(student))

display_students(students)