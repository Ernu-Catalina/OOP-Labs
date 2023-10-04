from Class import Student, Date, Faculty


class FacultyFunctions:
    faculty_list = []
    faculty_file_path = 'faculties.txt'  # Path to the faculty file
    students_file_path = 'students.txt'  # Path to the students file

    @staticmethod
    def add_student_to_file(student, faculty, students):
        with open('students.txt', 'a') as file:
            file.write(f"{student.f_name},{student.l_name},{student.mail},{student.b_day},{student.e_date}, {faculty.abb}\n")

    @staticmethod
    def load_students_from_file():
        try:
            with open(FacultyFunctions.students_file_path, 'r') as file:
                for line in file:
                    student_info = line.strip().split(',')
                    if len(student_info) == 6:
                        # Extracting information from the line
                        first_name, last_name, email, b_day, e_day, faculty_abbreviation = student_info

                        # Converting date strings to Date objects
                        birth_date = Date(*map(int, b_day.split('/')))
                        enrollment_date = Date(*map(int, e_day.split('/')))

                        # Finding the faculty by abbreviation
                        faculty = FacultyFunctions.find_faculty_by_abbreviation(faculty_abbreviation)

                        if faculty is not None:
                            new_student = Student(first_name, last_name, email, birth_date, enrollment_date, faculty)
                            faculty.add_student(new_student)
                            print(f"Student {first_name} {last_name} added to {faculty.abb} ({faculty.name}) successfully.")
                        else:
                            print(
                                f"Faculty {faculty_abbreviation} not found for student {first_name} {last_name}. Skipping.")
                    else:
                        print(f"Invalid format in the students file. Skipping line: {line}")

        except FileNotFoundError:
            print("Students file not found. Creating a new one.")

    @staticmethod
    def find_faculty_by_abbreviation(abbreviation):
        for faculty in FacultyFunctions.faculty_list:
            if faculty.abb == abbreviation:
                return faculty
        return None


