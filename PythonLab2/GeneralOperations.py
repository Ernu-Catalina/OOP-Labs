from Class import Faculty, Student, Date
from FacultyOperations import FacultyFunctions


class GeneralFunctions:
    faculty_list = []  # A class variable to store faculties
    faculty_file_path = 'faculties.txt'  # Path to the faculty file
    students_file_path = 'students.txt'  # Path to the students file

    @staticmethod
    def load_faculties_from_file():
        try:
            with open(GeneralFunctions.faculty_file_path, 'r') as file:
                for line in file:
                    faculty_name, faculty_abbreviation = line.strip().split(',')
                    new_faculty = Faculty(faculty_name, faculty_abbreviation)
                    GeneralFunctions.faculty_list.append(new_faculty)
        except FileNotFoundError:
            print("Faculty file not found. Creating a new one.")

    @staticmethod
    def load_students_from_file():
        try:
            with open(GeneralFunctions.students_file_path, 'r') as file:
                for line in file:
                    student_info = line.strip().split(',')
                    if len(student_info) == 6:
                        first_name, last_name, email, b_day, e_day, faculty_abbreviation = student_info

                        birth_date = Date(*map(int, b_day.split('/')))
                        enrollment_date = Date(*map(int, e_day.split('/')))

                        faculty = GeneralFunctions.find_faculty_by_abbreviation(faculty_abbreviation)

                        if faculty is not None:
                            new_student = Student(first_name, last_name, email, birth_date, enrollment_date, faculty)
                            faculty.add_student(new_student)
                        else:
                            print(
                                f"Faculty {faculty_abbreviation} not found for student {first_name} {last_name}. Skipping.")
                    else:
                        print(f"Invalid format in the students file. Skipping line: {line}")

        except FileNotFoundError:
            print("Students file not found. Creating a new one.")

    @staticmethod
    def create_student():
        student_first_name = input("Enter student's first name: ")
        student_last_name = input("Enter student's last name: ")
        student_email = input("Enter student's email: ")

        b_day = input("Enter student's birth date (DD/MM/YYYY): ")
        birth_date = Date(*map(int, b_day.split('/')))

        e_day = input("Enter student's enrollment date (DD/MM/YYYY): ")
        enrollment_date = Date(*map(int, e_day.split('/')))

        GeneralFunctions.load_faculties_from_file()
        faculty_abbreviation_to_search = input("Enter faculty abbreviation: ")

        faculty = GeneralFunctions.find_faculty_by_abbreviation(faculty_abbreviation_to_search)

        if faculty is None:
            create_faculty = input(f"Faculty {faculty_abbreviation_to_search} does not exist. Do you want to create it? (Y/N) ")
            if create_faculty.lower() == 'y':
                faculty = GeneralFunctions.create_faculty()
                if faculty is not None:
                    print(f"\nFaculty {faculty.abb} ({faculty.name}) created successfully!")
                else:
                    print("Failed to create faculty. Student not added.")
                    return
            else:
                print(f"\nFaculty {faculty_abbreviation_to_search} not found. Student not added.")
                return

        new_student = Student(student_first_name, student_last_name, student_email, birth_date, enrollment_date,faculty)
        faculty.add_student(new_student)
        FacultyFunctions.add_student_to_file(new_student, faculty.students)

    @staticmethod
    def create_faculty():
        faculty_name = input("Enter the faculty name: ")
        faculty_abbreviation = input(f"Enter abbreviation for {faculty_name}: ")

        new_faculty = Faculty(faculty_name, faculty_abbreviation)
        GeneralFunctions.faculty_list.append(new_faculty)

        print(f"\nFaculty {new_faculty.abb} ({new_faculty.name}) created successfully!")

        # Save faculties to file after creating a new faculty
        GeneralFunctions.save_faculties_to_file()

        return new_faculty

    @staticmethod
    def find_faculty_by_name(faculty_name):
        for faculty in GeneralFunctions.faculty_list:
            if faculty.name == faculty_name.upper():
                return faculty
        return None

    @staticmethod
    def find_faculty_by_abbreviation(faculty_abbreviation):
        for faculty in GeneralFunctions.faculty_list:
            if faculty.abb == faculty_abbreviation.upper():
                return faculty
        return None

    @staticmethod
    def save_faculties_to_file():
        with open(GeneralFunctions.faculty_file_path, 'w') as file:
            for faculty in GeneralFunctions.faculty_list:
                file.write(f"{faculty.name},{faculty.abb}\n")

    @staticmethod
    def mark_student_as_graduated(student_name):
        for faculty in GeneralFunctions.faculty_list:
            for student in faculty.students:
                if f"{student.f_name} {student.l_name}" == student_name:
                    student.graduate()
                    print(f"{student_name} has been marked as graduated.")
                    return True

        print(f"Student {student_name} not found.")
        return False
