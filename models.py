from data_manager import read_data, write_data


class Student:

    def __init__(self, name, email):

        self.name = name
        self.email = email

    def save(self):

        students = read_data('data/students.json')

        student = {
            "id": len(students) + 1,
            "name": self.name,
            "email": self.email
        }

        students.append(student)

        write_data('data/students.json', students)


class Course:

    def __init__(self, course_name, instructor):

        self.course_name = course_name
        self.instructor = instructor

    def save(self):

        courses = read_data('data/courses.json')

        course = {
            "id": len(courses) + 1,
            "course_name": self.course_name,
            "instructor": self.instructor
        }

        courses.append(course)

        write_data('data/courses.json', courses)


class Enrollment:

    def __init__(self, student_id, course_id):

        self.student_id = student_id
        self.course_id = course_id

    def save(self):

        enrollments = read_data('data/enrollments.json')

        enrollment = {
            "student_id": self.student_id,
            "course_id": self.course_id
        }

        enrollments.append(enrollment)

        write_data('data/enrollments.json', enrollments)