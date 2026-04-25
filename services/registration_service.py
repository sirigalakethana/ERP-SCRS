def check_prereq(student, course):
    for p in course.prereqs:
        if p and p not in student.completed:
            return False
    return True

def check_clash(student, course):
    for c in student.registered:
        if c.day == course.day and c.time == course.time:
            return True
    return False

def register_course(student, course):
    if not check_prereq(student, course):
        print("Prerequisite not satisfied")
        return

    if course.seats <= 0:
        print("No seats available")
        return

    if check_clash(student, course):
        print("Timetable clash detected")
        return

    student.registered.append(course)
    course.seats -= 1
    print("Registered successfully")

def drop_course(student, code):
    for c in student.registered:
        if c.code == code:
            student.registered.remove(c)
            c.seats += 1
            print("Course dropped")
            return
    print("Course not found")