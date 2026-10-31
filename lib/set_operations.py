# This module contains operations related to sets.
stds = [
   (101, "Miles", "Mathematics"),
    (102, "Laura", "Mathematics"),
    (103, "Benji", "Physics"),
    (104, "Natalia", "Physics"),
    (105, "Nadia", "Mathematics"),
]

def unique_majors(student_list):
    unique_sdts = {uniq[2] for uniq in student_list}
    return unique_sdts
    """
    Return a set of unique student majors using set comprehension.
    Extract the major field from each student record.
    """
    pass
print(unique_majors(stds))