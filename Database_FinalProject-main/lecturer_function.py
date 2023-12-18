from sql_queries import *
import time
import os


def view_courses(lecturer_id):
    # Fetch courses taught by the lecturer based on lecturer_id
    lecturer_courses = get_lecturer_courses(lecturer_id)
    os.system('cls')

    if not lecturer_courses:
        print("You are not currently teaching any courses.")
        input("\nPress Enter to return to the menu...")
        return

    print("\nCourses Taught:")
    print("--------------------------------------------------------------\n")
    for course in lecturer_courses:
        print(f">[{course[0]}] {course[1]}\n")

    print("--------------------------------------------------------------")
    selected_course_id = input("Enter the ID of the course to view students (or '0' to go back): ")

    if selected_course_id == '0':
        return
    elif not selected_course_id.isdigit():
        print("Invalid input. Please enter a valid course ID.")
        input("\nPress Enter to continue...")
        view_courses(lecturer_id)
    else:
        selected_course_id = int(selected_course_id)
        view_students_in_course(lecturer_id, selected_course_id)


def view_students_in_course(lecturer_id, course_id):
    os.system('cls')
    # Fetch students enrolled in the selected course with grades
    students_in_course = get_students_in_course_with_grades(lecturer_id, course_id)

    if not students_in_course:
        print("No students enrolled in this course.")
    else:
        print("\nStudents Enrolled in the Course:")
        print("--------------------------------------------------------------\n")
        print("{:<5} {:<20} {:<10} {:<10}".format("ID", "Name", "Grade", "Numerical Grade"))
        print("-" * 62)
        
        for student in students_in_course:
            student_id, student_name, grade, numerical_grade = student
            print("{:<5} {:<20} {:<10} {:<10}".format(student_id, student_name, grade, f"{numerical_grade}\n"))

    input("\nPress Enter to return to the menu...")




def edit_student_grade(lecturer_id):
    os.system('cls')
    # Display courses taught by the lecturer
    lecturer_courses = get_lecturer_courses(lecturer_id)

    if not lecturer_courses:
        print("You are not currently teaching any courses.")
        input("\nPress Enter to return to the menu...")
        return

    print("\nCourses Taught:")
    print("--------------------------------------------------------------\n")
    for course in lecturer_courses:
        print(f">[{course[0]}] {course[1]}\n")

    print("--------------------------------------------------------------")
    course_id_to_edit = input("Enter the ID of the course you'd like to edit (or '0' to go back): ")

    if course_id_to_edit == '0':
        return

    if not course_id_to_edit.isdigit():
        print("Invalid input. Please enter a valid course ID.")
        time.sleep(2)
        edit_student_grade(lecturer_id)
    else:
        course_id_to_edit = int(course_id_to_edit)

        # Fetch students and their grades in the selected course
        students_in_course = get_students_in_course_with_grades(lecturer_id, course_id_to_edit)

        if not students_in_course:
            print("No students enrolled in this course.")
        else:
            print("--------------------------------------------------------------")
            print("Students Enrolled in the Course:")
            print("--------------------------------------------------------------\n")
            print("{:<5} {:<20} {:<10} {:<10}".format("ID", "Name", "Grade", "Numerical Grade"))
            print("-" * 62)
        
            for student in students_in_course:
                student_id, student_name, grade, numerical_grade = student
                print("{:<5} {:<20} {:<10} {:<10}".format(student_id, student_name, grade, f"{numerical_grade}\n"))

        # Get input for the student and the new grade
        student_id_to_edit = input("\nEnter the ID of the student to edit the grade (or '0' to go back): ")

        if student_id_to_edit == '0':
            return

        if not student_id_to_edit.isdigit():
            print("Invalid input. Please enter a valid student ID.")
            time.sleep(2)
            edit_student_grade(lecturer_id)
        else:
            student_id_to_edit = int(student_id_to_edit)

            new_grade = input(f"Enter the new grade for the student with ID {student_id_to_edit}: ")

            # Update the grade in the database
            update_student_grade(student_id_to_edit, course_id_to_edit, new_grade)

            print(f"Grade for student with ID {student_id_to_edit} in course {course_id_to_edit} updated successfully.")

            input("\nPress Enter to return to the menu...")


def edit_mode(lecturer_id):
    os.system('cls')
    print("Edit Mode - You can edit the data of students in their respective courses.")
    edit_student_grade(lecturer_id)

