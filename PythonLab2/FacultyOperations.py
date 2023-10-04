from Class import Student, Date, Faculty


class FacultyFunctions:
    faculty_list = []
    faculty_file_path = 'faculties.txt'  # Path to the faculty file
    students_file_path = 'students.txt'  # Path to the students file

    @staticmethod
    def save_students_to_file(student_list):
        with open('students.txt', 'w') as file:
            for student in student_list:
                file.write(
                    f"{student.f_name},{student.l_name},{student.mail},{student.b_day},{student.e_date},{student.faculty.abb},{int(student.graduated)}\n")
                pass


