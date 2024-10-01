student_grades = {"Mat":88,
    "gab":90,
    "rei":99,
    "roger":87,
    "bruum":91,
}
print(student_grades)
print("Grade of third student",student_grades ["gab"])
student_grades ["rei"] = "90"
print(student_grades)
del student_grades["bruum"]
print(student_grades)
print("Last student and grade:", list(student_grades.items())[-1])