from Class import Student, Faculty, Date
from FacultyOperations import FacultyFunctions
from GeneralOperations import GeneralFunctions
from LoadingOperations import LoadingFunctions

print("Welcome to our Program! What would you like to do?")

while True:
    print("\nTo access General Operations, please type 'G'.")
    print("To access Faculty Operations, please type 'F'.")
    print("To quit the program, please type 'Q'.")

    operation = input().lower()

    if operation == 'g':
        print("You have chosen General Operations.")
        print("\nTo create a new faculty, please type NF.")
        print("To display what faculty a student belongs to, please type SF.")
        print("To display all university faculties, please type DF.")
        print("To display all university faculties in a particular field, please type DFF.")
        print("To quit the program all together, please type Q.")

    elif operation == 'f':
        print("You have chosen Faculty Operations.")
        print("\nTo add new students, please type AS.")
        print("To graduate an already existing student, please type GS.")
        print("To display all students who are currently enrolled, please type DS.")
        print("To display all students who have graduated, please type DGS.")
        print("To check if a student belongs to a specific faculty, please type CSF.")
        print("To quit the program all together, please type Q.")

    elif operation == 'q':
        print("Quitting the program. Goodbye!")
        break

    else:
        print("Invalid input. Please try again.")


# FACULTY OPERATIONS:

    faculty_functions = FacultyFunctions()
    operation = input().upper()

    if operation == 'AS':
        FacultyFunctions.create_student()
        LoadingFunctions.save_faculties_to_file()
        LoadingFunctions.load_student_faculties_from_file()
        LoadingFunctions.load_student_graduation_status_from_file()

    elif operation == 'GS':
        LoadingFunctions.load_faculties_from_file()
        LoadingFunctions.load_student_faculties_from_file()
        student_name = input("Enter the student name to mark as graduated: ")
        success = GeneralFunctions.mark_student_as_graduated(student_name)
        if success:
            LoadingFunctions.save_faculties_to_file()
        else:
            print("Operation unsuccessful. No changes made.")

    elif operation == 'DS':
        enrolled_students, graduated_students = LoadingFunctions.load_student_graduation_status_from_file()
        print("\nList of currently enrolled students:")
        for student in enrolled_students:
            print(f"{student.f_name} {student.l_name} - {student.mail}, Birth Date: {student.b_day}, Enrollment Date: {student.e_date}")

    elif operation == 'DGS':
        enrolled_students, graduated_students = LoadingFunctions.load_student_graduation_status_from_file()
        print("\nList of graduated students:")
        for student in graduated_students:
            print(f"{student.f_name} {student.l_name} - {student.mail}, Birth Date: {student.b_day}, Enrollment Date: {student.e_date}")

    elif operation == 'Q':
        print("Quitting the program. Goodbye!")
        break


# GENERAL OPERATIONS:

    general_functions = GeneralFunctions()

    if operation == 'NF':
        LoadingFunctions.load_faculties_from_file()
        GeneralFunctions.create_faculty()
        LoadingFunctions.save_faculties_to_file()

