from Class import Faculty, Student, Date, StudyFields
from LoadingOperations import LoadingFunctions


class GeneralFunctions:

    @staticmethod
    def create_faculty():
        faculty_name = input("Enter the faculty name: ")
        faculty_abbreviation = input(f"Enter abbreviation for {faculty_name}: ")

        print("Choose a study field for the faculty:")
        for field in StudyFields:
            print(f"{field.value}. {field.name}")

        while True:
            try:
                choice = int(input("Enter the number associated with the chosen study field: "))
                study_field = next(f for f in StudyFields if f.value == choice)
                break
            except (ValueError, TypeError, StopIteration):
                print("Invalid choice. Please enter a valid number.")

        new_faculty = Faculty(faculty_name, faculty_abbreviation, study_field)
        LoadingFunctions.faculty_list.append(new_faculty)
        print(f"\nFaculty {new_faculty.abb} ({new_faculty.name}) created successfully!")

        LoadingFunctions.save_faculties_to_file()
        return new_faculty

    @staticmethod
    def find_faculty_by_name(faculty_name):
        for faculty in LoadingFunctions.faculty_list:
            if faculty.name == faculty_name.upper():
                return faculty
        return None

    @staticmethod
    def mark_student_as_graduated(student_name):
        LoadingFunctions.load_student_faculties_from_file()
        student = None

        for faculty in LoadingFunctions.faculty_list:
            for s in faculty.students:
                if f"{s.f_name} {s.l_name}".lower() == student_name.lower():
                    student = s
                    break

        if student:
            if not student.graduated:
                student.graduate()
                print(f"Student {student_name} has been marked as graduated.")
                LoadingFunctions.save_students_to_file(LoadingFunctions.student_list)

                return True
            else:
                print(f"Student {student_name} is already marked as graduated.")
        else:
            print(f"No student found with the name {student_name}.")

        return False

    @staticmethod
    def get_all_students():
        all_students = []
        for faculty in LoadingFunctions.faculty_list:
            all_students.extend(faculty.students)
        return all_students

    @staticmethod
    def get_student_faculty_info(student_name):
        LoadingFunctions.load_student_faculties_from_file()
        for faculty in LoadingFunctions.faculty_list:
            for s in faculty.students:
                if f"{s.f_name} {s.l_name}" == student_name:
                    return f"Student {student_name} belongs to {faculty.name} ({faculty.abb})."

        return f"No student found with the name {student_name}."

    @staticmethod
    def display_all_university_faculties():
        LoadingFunctions.load_faculties_from_file()

        if LoadingFunctions.faculty_list:
            print("List of All University Faculties:")
            for faculty in LoadingFunctions.faculty_list:
                print(f"{faculty.name} ({faculty.abb})")
        else:
            print("No faculties found in the university.")
