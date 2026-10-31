# This module contains functions to lazily generate student data.
students = [
    (101, "Alice Johnson", "Computer Science"),
    (102, "Bob Smith", "Mathematics"),
    (103, "Charlie Davis", "Physics"),
    (104, "David Wilson", "Computer Science"),
    (105, "Eve Lewis", "Mathematics"),
]
def student_generator(student_list, major):
    return (student for student in student_list if major.lower() == student[2].lower())
    """
    Generate student records filtered by major lazily for memory efficiency
    using a Python generator.
    """
    pass
science_courses = student_generator(students, "Mathematics")
print(next(science_courses))
print(next(science_courses))

