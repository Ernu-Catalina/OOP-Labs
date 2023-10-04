from Class import Student, Date, Faculty
from LoadingOperations import LoadingFunctions
from GeneralOperations import GeneralFunctions

class FacultyFunctions:

    @staticmethod
    def create_student():
        student_first_name = input("Enter student's first name: ")
        student_last_name = input("Enter student's last name: ")
        student_email = input("Enter student's email: ")

        b_day = input("Enter student's birth date (DD/MM/YYYY): ")
        birth_date = Date(*map(int, b_day.split('/')))

        e_day = input("Enter student's enrollment date (DD/MM/YYYY): ")
        enrollment_date = Date(*map(int, e_day.split('/')))

        LoadingFunctions.load_faculties_from_file()
        faculty_abbreviation_to_search = input("Enter faculty abbreviation: ")

        faculty = LoadingFunctions.find_faculty_by_abbreviation(faculty_abbreviation_to_search)

        if faculty is None:
            create_faculty = input(
                f"Faculty {faculty_abbreviation_to_search} does not exist. Do you want to create it? (Y/N) ")
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

        # Set graduation status to False upon creation
        new_student = Student(student_first_name, student_last_name, student_email, birth_date, enrollment_date, faculty)
        faculty.add_student(new_student)
        LoadingFunctions.save_students_to_file(faculty.students)

        print(f"Student {new_student.f_name} {new_student.l_name} added successfully.")


