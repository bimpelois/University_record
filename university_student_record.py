AVAILABLE_COURSES = {
    "Math", "Physics", "Computer Science", "Biology", "Chemistry",
    "Statistics", "English", "Economics", "History", "Philosophy",
    "Sociology", "Political Science", "Geography", "Psychology", "Art",
    "Music", "Engineering", "Law", "Medicine", "Business"
}

students = {}

def establish_student():
    username = input("Enter your username: ")

    if username in students:
        print("Username already exists.")
        return

    name = input("Enter name: ")
    age = int(input("Enter age: "))

    courses_input = input("Enter courses (comma separated): ").split(",")
    courses = set()

    for course in courses_input:
        course = course.strip()
        if course in AVAILABLE_COURSES:
            courses.add(course)
        else:
            print(course, "is not allowed and was skipped.")

    city = input("Enter city: ")
    zip_code = input("Enter zip code: ")

    students[username] = {
        "name": name,
        "age": age,
        "courses": courses,
        "address": {
            "city": city,
            "zip": zip_code
        }
    }

    print("Student added successfully.")

def display_student(username):
    if username in students:
        print(students[username])
    else:
        print("Student not found.")

def display_courses(username):
    if username in students:
        print(students[username]["courses"])
    else:
        print("Student not found.")


def display_zip(username):
    if username in students:
        print(students[username]["address"]["zip"])
    else:
        print("Student not found.")

def display_city(username):
    if username in students:
        print(students[username]["address"]["city"])
    else:
        print("Student not found.")


def add_course(username):
    if username in students:
        course = input("Enter course to add: ")

        if course not in AVAILABLE_COURSES:
            print("Course not offered.")
        elif course in students[username]["courses"]:
            print("Course already exists.")
        else:
            students[username]["courses"].add(course)
            print("Course added.")
    else:
        print("Student not found.")

def update_course(username):
    if username in students:
        old_course = input("Enter course to remove/update: ")

        if old_course in students[username]["courses"]:
            students[username]["courses"].remove(old_course)

            new_course = input("Enter new course (or press Enter to skip): ")

            if new_course:
                if new_course in AVAILABLE_COURSES:
                    students[username]["courses"].add(new_course)
                    print("Course updated.")
                else:
                    print("Invalid course. Old course removed only.")
            else:
                print("Course removed.")
        else:
            print("Course not found.")
    else:
        print("Student not found.")

def update_student(username):
    if username in students:
        name = input("Enter new name (press Enter to skip): ")
        age = int(input("Enter new age (press Enter to skip): "))
        city = input("Enter new city (press Enter to skip): ")
        zip_code = input("Enter new zip code (press Enter to skip): ")

        if name:
            students[username]["name"] = name
        if age:
            students[username]["age"] = int(age)
        if city:
            students[username]["address"]["city"] = city
        if zip_code:
            students[username]["address"]["zip"] = zip_code

        print("Student updated.")
    else:
        print("Student not found.")

def total_students():
    print("Total students:", len(students))

