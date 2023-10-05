from enum import Enum


class Student:
    def __init__(self, first_name, last_name, email, birth_date, enrollment_date, faculty, graduated):
        self.f_name = first_name
        self.l_name = last_name
        self.mail = email
        self.b_day = birth_date
        self.e_date = enrollment_date
        self.faculty = faculty
        self.graduated = graduated

    def graduate(self):
        self.graduated = True


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"


class Faculty:
    def __init__(self, name, abbreviation, study_field):
        self.name = name
        self.abb = abbreviation
        self.students = []
        self.study_field = study_field

    def add_student(self, student):
        self.students.append(student)


class StudyFields(Enum):
    MECHANICAL_ENGINEERING = 1
    SOFTWARE_ENGINEERING = 2
    FOOD_TECHNOLOGY = 3
    URBANISM_ARCHITECTURE = 4
    VETERINARY_MEDICINE = 5



