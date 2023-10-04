from Class import Student, Faculty
from GeneralOperations import GeneralFunctions
from FacultyOperations import FacultyFunctions

print("Welcome to our Program! What would you like to do?")

#while True:
print("\nTo access our General Operations, please type G.")
print("To access our Faculty Operations, please type F.")

operation = input()

if operation.lower() == 'g':
    print("You have chosen General Operations.")
    print("\nTo create a new faculty, please type NF.")
    print("To display what faculty a student belongs to, please type SF.")
    print("To display all university faculties, please type DF.")
    print("To display all university faculties in a particular field, please type DFF.")
    print("To quit back to Main Menu, please type M.")
    print("To quit the program all together, please type Q.")
elif operation.lower() == 'f':
    print("You have chosen Faculty Operations.")
    print("\nTo add new students, please type AS.")
    print("To graduate an already existing student, please type GS.")
    print("To display all students who are currently enrolled, please type DES.")
    print("To display all students who have graduated, please type DGS.")
    print("To check if a student belongs to a specific faculty, please type CSF.")
    print("To quit back to Main Menu, please type M.")
    print("To quit the program all together, please type Q.")
else:
    print("Input not valid.")

operation = input()

if operation == 'NF' or operation == 'nf':
    g_functions = GeneralFunctions()
    faculty = g_functions.create_faculty()
    print(f"\nYou have successfully added the faculty {faculty.abb} ({faculty.name}).")
    print(f"\nWould you like to add students to this faculty?(Y/N)")
    ans = input()
    if ans.lower() == 'y':
        f_operations = FacultyFunctions()
        student_first_name_to_check = input("What is the student's first name? ")
        student_last_name_to_check = input("What is the student's last name? ")
        exists = f_operations.student_exists(faculty, student_first_name_to_check, student_last_name_to_check)

        if exists:
            print(f"{student_first_name_to_check} {student_last_name_to_check} is a student in this faculty.")
        else:
            print(f"{student_first_name_to_check} {student_last_name_to_check} is not a student in this faculty.")


elif operation == 'SF' or operation == 'sf':
    g_functions = GeneralFunctions()
    faculty = g_functions.create_faculty()
    print(f"\nYou have successfully added the Faculty {faculty.abb} ({faculty.name}).")


