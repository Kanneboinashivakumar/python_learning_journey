courses = {
    "python": {"shiva", "rahul", "priya"},
    "java": {"anil", "sai", "ram"},
    "c": {"kiran", "teja", "vijay"}
}

course = input("Enter course name: ").lower()
student = input("Enter student name: ").lower()

if course in courses:
    if student in courses[course]:
        print(student.title(), "is enrolled in", course.title())
    else:
        print(student.title(), "is not enrolled in", course.title())
else:
    print("Course not found")