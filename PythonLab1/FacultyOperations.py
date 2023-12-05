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
        faculty_abbreviation_to_search = input("Enter faculty abbreviation: ").upper()
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

        new_student = Student(student_first_name, student_last_name, student_email, birth_date, enrollment_date, faculty, False)

        existing_student = next((s for s in LoadingFunctions.student_list if s.f_name == new_student.f_name and s.l_name == new_student.l_name), None)

        if existing_student:
            existing_student.mail = new_student.mail
            existing_student.b_day = new_student.b_day
            existing_student.e_date = new_student.e_date
            existing_student.faculty = new_student.faculty  # Update faculty as well
            print(f"\nStudent {new_student.f_name} {new_student.l_name} already exists. Updated successfully!")
        else:
            LoadingFunctions.student_list.append(new_student)
            print(f"\nStudent {new_student.f_name} {new_student.l_name} created successfully!")

        LoadingFunctions.save_students_to_file(LoadingFunctions.student_list)

        return new_student

    @staticmethod
    def does_student_belong_to_faculty(student_name, faculty_abbreviation):
        LoadingFunctions.load_student_faculties_from_file()
        student = None
        for faculty in LoadingFunctions.faculty_list:
            for s in faculty.students:
                if f"{s.f_name} {s.l_name}".lower() == student_name.lower():
                    student = s
                    break
        if student:
            if student.faculty.abb == faculty_abbreviation.upper():
                return f"Yes, {student.f_name} {student.l_name} belongs to {faculty_abbreviation.upper()}."
            else:
                return f"No, {student.f_name} {student.l_name} does not belong to {faculty_abbreviation.upper()}."
        else:
            return f"No student found with the name {student_name}."


