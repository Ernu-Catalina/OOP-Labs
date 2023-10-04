from Class import Faculty, Student, Date, StudyFields
from LoadingOperations import LoadingFunctions


class GeneralFunctions:

    @staticmethod
    def create_faculty():
        faculty_name = input("Enter the faculty name: ")
        faculty_abbreviation = input(f"Enter abbreviation for {faculty_name}: ")
        print("Choose a study field for the faculty:")
        for field in StudyFields:
            print(f"{field.value[1]}. {field.value[0]}")
        while True:
            try:
                choice = int(input("Enter the number associated with the chosen study field: "))
                study_field = next(f for f in StudyFields if f.value[1] == choice)
                break
            except (ValueError, TypeError, StopIteration):
                print("Invalid choice. Please enter a valid number.")
        new_faculty = Faculty(faculty_name, faculty_abbreviation, study_field)
        LoadingFunctions.faculty_list.append(new_faculty)
        print(f"\nFaculty {new_faculty.abb} ({new_faculty.name}) created successfully!")
        # Save faculties to file after creating a new faculty
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
        for faculty in LoadingFunctions.faculty_list:
            for student in faculty.students:
                if f"{student.f_name} {student.l_name}" == student_name:
                    student.graduate()
                    LoadingFunctions.save_students_to_file(GeneralFunctions.get_all_students())
                    print(f"{student_name} has been marked as graduated.")
                    return True

        print(f"Student {student_name} not found.")
        return False

    @staticmethod
    def get_all_students():
        all_students = []
        for faculty in LoadingFunctions.faculty_list:
            all_students.extend(faculty.students)
        return all_students
