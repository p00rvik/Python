def print_student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_student_info(name="Alice", age=22, major="Computer Science")
print_student_info(name="Bob", age=25, city="Mysuru", GPA=3.8)
