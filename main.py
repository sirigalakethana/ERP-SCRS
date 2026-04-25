from models.student import Student
from models.course import Course
from services.registration_service import register_course, drop_course
from services.analytics_service import show_analytics

courses = []

n = int(input("Enter number of courses: "))

for i in range(n):
    print("\nEnter Course Details:")
    code = input("Code: ")
    name = input("Name: ")
    seats = int(input("Seats: "))
    day = input("Day: ")
    time = input("Time: ")
    pr = input("Prereqs (comma): ")
    prereqs = pr.split(",") if pr else []

    courses.append(Course(code, name, seats, day, time, prereqs))

sid = input("\nEnter Student ID: ")
name = input("Enter Student Name: ")
completed = input("Completed courses (comma): ").split(",")

student = Student(sid, name, completed)

while True:
    print("\n1.View Courses\n2.Register\n3.Drop\n4.View Registered\n5.Analytics\n6.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        for c in courses:
            print(c.code, c.name, c.seats, c.day, c.time)

    elif ch == "2":
        code = input("Enter course code: ")
        for c in courses:
            if c.code == code:
                register_course(student, c)

    elif ch == "3":
        code = input("Enter course code: ")
        drop_course(student, code)

    elif ch == "4":
        print("\nRegistered Courses:")
        for c in student.registered:
            print(c.code, c.name)

    elif ch == "5":
        show_analytics(courses)

    elif ch == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice")