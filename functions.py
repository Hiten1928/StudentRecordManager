students = []

def get_student_titlecase():
    students_titlecase = []
    for student in students:
        students_temp= student.get("name")
        students_titlecase = students_temp.title()

    return students_titlecase


def print_student_titlecase():
    student_titlecase = get_student_titlecase()
    #print_student_titlecase(student_titlecase)


def add_student(name,  student_attendance, student_course_taken, student_id=00000):
    student = {"name": name, "student_id": student_id, "student attendance": student_attendance, "student_course_taken": student_course_taken}
    students.append(student)


name = raw_input("Enter Student Name : ")
student_id = input("Enter Student ID: ")
student_attendance = input("Enter Student's Attendance: ")
student_course_taken = raw_input("Enter Course Taken by student: ")


add_student(name, student_id, student_attendance, student_course_taken)
student_list = get_student_titlecase()
print_student_titlecase()