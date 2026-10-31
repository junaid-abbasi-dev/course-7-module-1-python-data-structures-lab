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
    """
    Format student data for display.
    The function should return a formatted string containing:
    - Student ID
    - Student Name
    - Major
    such as: "ID: 10 | Name: Louis Medina | Major: Computer Science"
    """
    pass

def display_students(student_list):
    for student in student_list:
        print(format_student_data(student))
    """
    Display all student records.
    Loop through the student_list and print each student using format_student_data().
    """
    pass

display_students(students)