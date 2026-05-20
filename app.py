from flask import Flask, render_template, request, redirect

from models import Student, Course, Enrollment
from data_manager import read_data

app = Flask(__name__)


@app.route('/')
def home():

    return render_template('index.html')


@app.route('/register_student', methods=['GET', 'POST'])
def register_student():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']

        student = Student(name, email)
        student.save()

        return redirect('/students')

    return render_template('register_student.html')


@app.route('/add_course', methods=['GET', 'POST'])
def add_course():

    if request.method == 'POST':

        course_name = request.form['course_name']
        instructor = request.form['instructor']

        course = Course(course_name, instructor)
        course.save()

        return redirect('/courses')

    return render_template('add_course.html')


@app.route('/enroll', methods=['GET', 'POST'])
def enroll():

    students = read_data('data/students.json')
    courses = read_data('data/courses.json')

    if request.method == 'POST':

        student_id = request.form['student_id']
        course_id = request.form['course_id']

        enrollment = Enrollment(student_id, course_id)
        enrollment.save()

        return redirect('/enrollments')

    return render_template(
        'enroll.html',
        students=students,
        courses=courses
    )


@app.route('/students')
def students():

    students = read_data('data/students.json')

    return render_template(
        'students.html',
        students=students
    )


@app.route('/courses')
def courses():

    courses = read_data('data/courses.json')

    return render_template(
        'courses.html',
        courses=courses
    )


@app.route('/enrollments')
def enrollments():

    enrollments = read_data('data/enrollments.json')

    return render_template(
        'enrollments.html',
        enrollments=enrollments
    )


if __name__ == '__main__':

    app.run(debug=True)