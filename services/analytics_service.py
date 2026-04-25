import matplotlib.pyplot as plt

def show_analytics(courses):
    names = []
    values = []

    for c in courses:
        names.append(c.name)
        val = int(input(f"Enter enrolled students for {c.name}: "))
        values.append(val)

    plt.bar(names, values)
    plt.title("Course Enrollment")
    plt.xlabel("Courses")
    plt.ylabel("Students")
    plt.show()