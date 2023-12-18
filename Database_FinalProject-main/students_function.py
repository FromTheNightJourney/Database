from sql_queries import *
import os
from current_time import *


def display_student_grades_from_db(student_id):
    student_data = get_student_data_by_id(student_id)
    os.system('cls')

    if not student_data:
        print("Student not found.")
        return

    print(f"\nStudent: {student_data[1]}")
    print("\nCourse Grades:\n")

    grades_data = get_student_grades(student_id)

    if not grades_data:
        print("No grades available.")
    else:
        for grade_data in grades_data:
            course_id = grade_data[2]
            course_data = get_course_data_by_id(course_id)

            if not course_data:
                print(f"Course ID {course_id}: Unknown Course")
            else:
                print(f"Course ID {course_id}: {course_data[1]}")
                print(f"   >Grade: {grade_data[3]} ({grade_data[4]})\n")

    input("\nPress Enter to return to the menu...")


def display_student_info(student_id):
    student_data = get_student_data_by_id(student_id)
    os.system('cls')
    print("\n\
Good " + greeting + f", {student_data[1]}! Welcome to the Ouval Academy Database. \n\
It is currently " + TwoFourHrClock + ".\n")

    if not student_data:
        print("Student not found.")
        input("\nPress Enter to return to the menu...")
        return

    print("+" + "-"*63 + "+")
    print("|   {:^60}|".format("Student Information"))
    print("+" + "-"*63 + "+")
    print("|   {:<60}|".format(""))
    print("|   {:<60}|".format(f"ID: {student_data[0]}"))
    print("|   {:<60}|".format(f"Name: {student_data[1]}"))
    print("|   {:<60}|".format(f"Date of Birth: {student_data[2]}"))
    print("|   {:<60}|".format(f"Gender: {student_data[3]}"))
    print("|   {:<60}|".format(f"Address: {student_data[4]}"))
    print("|   {:<60}|".format(f"Phone Number: {student_data[5]}"))
    print("|   {:<60}|".format(f"Email Address: {student_data[6]}"))
    print("|   {:<60}|".format(f"Major: {student_data[7]}"))
    print("|   {:<60}|".format(f"Year of Study: {student_data[8]}"))
    print("|   {:<60}|".format(f"Admission Date: {student_data[9]}"))
    print("|   {:<60}|".format(""))
    print("+" + "-"*63 + "+")

    input("\n\
\nTo return to the menu, simply press Enter.\n\
-----------------------------------------------------------------\n")