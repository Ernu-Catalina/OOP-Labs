from Class import Faculty, Student, Date, StudyFields


class LoadingFunctions:
    faculty_list = []
    faculty_file_path = 'faculties.txt'
    students_file_path = 'students.txt'

    @staticmethod
    def get_study_field(number):
        for field in StudyFields:
            if field.value[1] == number:
                return field
        return None

    @staticmethod
    def find_faculty_by_abbreviation(abbreviation):
        for faculty in LoadingFunctions.faculty_list:
            if faculty.abb == abbreviation:
                return faculty
        return None

    @staticmethod
    def load_faculties_from_file():
        try:
            with open(LoadingFunctions.faculty_file_path, 'r') as file:
                for line in file:
                    faculty_name, faculty_abbreviation, study_field_number = line.strip().split(',')
                    study_field = LoadingFunctions.get_study_field(int(study_field_number))
                    if study_field:
                        new_faculty = Faculty(faculty_name, faculty_abbreviation, study_field)
                        LoadingFunctions.faculty_list.append(new_faculty)
                    else:
                        print(f"Invalid study field number {study_field_number}. Skipping this line.")

        except FileNotFoundError:
            print("Faculty file not found. Creating a new one.")

    @staticmethod
    def load_student_faculties_from_file():
        try:
            # Load faculties first
            LoadingFunctions.load_faculties_from_file()

            with open(LoadingFunctions.students_file_path, 'r') as file:
                for line in file:
                    student_info = line.strip().split(',')
                    if len(student_info) == 7:
                        faculty_abbreviation = student_info[5]
                        # Find the faculty by abbreviation
                        faculty = LoadingFunctions.find_faculty_by_abbreviation(faculty_abbreviation)
                        if faculty is not None:
                            print(f"Student Faculty Loaded: {faculty.abb} ({faculty.name})")
                        else:
                            print(f"Faculty {faculty_abbreviation} not found for student. Skipping.")
                    else:
                        print(f"Invalid format in the students file. Skipping line: {line}")

        except FileNotFoundError:
            print("Students file not found. Creating a new one.")

    @staticmethod
    def load_student_graduation_status_from_file():
        enrolled_students = []
        graduated_students = []
        try:
            with open(LoadingFunctions.students_file_path, 'r') as file:
                for line in file:
                    student_info = line.strip().split(',')
                    if len(student_info) == 7:
                        first_name, last_name, email, b_day, e_day, faculty_abbreviation, graduated_str = student_info
                        birth_date = Date(*map(int, b_day.split('/')))
                        enrollment_date = Date(*map(int, e_day.split('/')))
                        faculty = LoadingFunctions.find_faculty_by_abbreviation(faculty_abbreviation)
                        graduated = bool(int(graduated_str))
                        new_student = Student(first_name, last_name, email, birth_date, enrollment_date, faculty, graduated)
                        if graduated:
                            graduated_students.append(new_student)
                        else:
                            enrolled_students.append(new_student)
                    else:
                        print(f"Invalid format in the students file. Skipping line: {line}")
        except FileNotFoundError:
            print("Students file not found. Creating a new one.")
        return enrolled_students, graduated_students

    @staticmethod
    def save_faculties_to_file():
        with open(LoadingFunctions.faculty_file_path, 'w') as file:
            for faculty in LoadingFunctions.faculty_list:
                file.write(f"{faculty.name},{faculty.abbreviation},{faculty.study_field.value[1]}\n")

    @staticmethod
    def save_students_to_file(student_list):
        with open('students.txt', 'w') as file:
            for student in student_list:
                file.write(
                    f"{student.f_name},{student.l_name},{student.mail},{student.b_day},{student.e_date},{student.faculty.abb},{int(student.graduated)}\n")
                pass
