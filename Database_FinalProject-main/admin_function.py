from sql_queries import *
import time


def add_course():
    # Get input for the new course
    course_name = input("Enter the name of the new course: ")
    course_description = input("Enter the course description: ")
    course_department = input("Enter the department of the course: ")
    course_credit_hours = input("Enter the amount of credit hours of the course: ")
    course_semester = input("Enter the semester of the course: ")

    print(f"Course Name: {course_name}")
    print(f"Course Description: {course_description}")
    print(f"Course Department: {course_department}")
    print(f"Course Credit Hours: {course_credit_hours}")
    print(f"Course Semester: {course_semester}")
    user_input = input("Proceed adding this new course? (y/n): ").lower()

    if user_input.lower() == 'y':
        # Insert the new course into the database
        insert_courses(course_name, course_department, course_credit_hours, course_semester, course_description, None)

        print(f"Course '{course_name}' added successfully.")
    else:
        print("Course addition canceled.")

    input("\nPress Enter to return to the menu...")


def delete_course():
    # Display courses
    all_courses = get_all_courses()

    if not all_courses:
        print("There are no courses in the database.")
        input("\nPress Enter to return to the menu...")
        return

    print("All Courses:")
    for course in all_courses:
        print(f"{course[0]}. {course[1]}")

    # Get input for the course to delete
    course_id_to_delete = input("\nEnter the ID of the course to delete (or '0' to go back): ")

    if course_id_to_delete == '0':
        return

    if not course_id_to_delete.isdigit():
        print("Invalid input. Please enter a valid course ID.")
        time.sleep(2)
        delete_course()
    else:
        course_id_to_delete = int(course_id_to_delete)

        # Confirm deletion with the user
        confirm_deletion = input(
            f"Are you sure you want to delete the course with ID {course_id_to_delete}? (y/n): ").lower()

        if confirm_deletion == 'y':
            delete_courses(course_id_to_delete)

            print(f"Course with ID {course_id_to_delete} deleted successfully.")
        else:
            print("Course deletion canceled.")

        input("\nPress Enter to return to the menu...")


def add_student():
    # Get input for the new student
    student_name = input("Enter the name of the new student: ")
    date_of_birth = input("Enter the date of birth (YYYY-MM-DD): ")
    gender = input("Enter the gender of the student: ")
    home_address = input("Enter the home address of the student: ")
    phone_number = input("Enter the phone number of the student: ")
    email_address = input("Enter the email address of the student: ")
    major = input("Enter the major of the student: ")
    year_of_study = input("Enter the year of study: ")
    admission_date = input("Enter the admission date (YYYY-MM-DD): ")

    print(f"Student Name: {student_name}")
    print(f"Date of Birth: {date_of_birth}")
    print(f"Gender: {gender}")
    print(f"Home Address: {home_address}")
    print(f"Phone Number: {phone_number}")
    print(f"Email Address: {email_address}")
    print(f"Major: {major}")
    print(f"Year of Study: {year_of_study}")
    print(f"Admission Date: {admission_date}")

    user_input = input("Proceed adding this new student? (y/n): ").lower()

    if user_input.lower() == 'y':
        # Insert the new student into the database
        insert_student(student_name, date_of_birth, gender, home_address, phone_number, email_address, major,
                       year_of_study, admission_date)

        print(f"Student '{student_name}' added successfully.")
    else:
        print("Student addition canceled.")

    input("\nPress Enter to return to the menu...")


def remove_student():
    # Get input for the student to remove
    student_id_to_remove = input("Enter the ID of the student to remove: ")

    if not student_id_to_remove.isdigit():
        print("Invalid input. Please enter a valid student ID.")
        remove_student()
    else:
        student_id_to_remove = int(student_id_to_remove)

        # Confirm deletion with the user
        confirm_deletion = input(
            f"Are you sure you want to remove the student with ID {student_id_to_remove}? (y/n): ").lower()

        if confirm_deletion == 'y':
            # Remove the student from the database
            delete_student(student_id_to_remove)

            print(f"Student with ID {student_id_to_remove} removed successfully.")
        else:
            print("Student removal canceled.")

        input("\nPress Enter to return to the menu...")


def add_student_to_course():
    # Get input for the new enrollment
    student_id = input("Enter the ID of the student to enroll: ")
    course_id = input("Enter the ID of the course to enroll the student in: ")
    semester = input("Enter the semester: ")
    year = input("Enter the year: ")
    registration_date = input("Enter the registration date: ")
    status = input("Enter the status: ")

    if not (student_id.isdigit() and course_id.isdigit()):
        print("Invalid input. Please enter valid student and course IDs.")
        add_student_to_course()
    else:
        student_id = int(student_id)
        course_id = int(course_id)

        # Check if the student and course exist
        if not student_exists(student_id) or not course_exists(course_id):
            print("Invalid student or course ID. Please check the IDs and try again.")
            add_student_to_course()
        else:
            # Insert the new enrollment into the database
            insert_student_to_course(student_id, course_id, semester, year, registration_date, status)

            print(f"Student with ID {student_id} enrolled in course with ID {course_id} successfully.")

    input("\nPress Enter to return to the menu...")


def delete_student_from_course():
    # Get input for the enrollment to delete
    student_id_to_remove = input("Enter the ID of the student to remove from the course: ")
    course_id_to_remove = input("Enter the ID of the course to remove the student from: ")

    if not (student_id_to_remove.isdigit() and course_id_to_remove.isdigit()):
        print("Invalid input. Please enter valid student and course IDs.")
        delete_student_from_course()
    else:
        student_id_to_remove = int(student_id_to_remove)
        course_id_to_remove = int(course_id_to_remove)

        # Check if the student and course exist
        if not student_exists(student_id_to_remove) or not course_exists(course_id_to_remove):
            print("Invalid student or course ID. Please check the IDs and try again.")
            delete_student_from_course()
        else:
            # Confirm deletion with the user
            confirm_deletion = input(
                f"Are you sure you want to remove student with ID {student_id_to_remove} from course with ID {course_id_to_remove}? (y/n): ").lower()

            if confirm_deletion == 'y':
                # Remove the student from the course in the database
                remove_student_from_course(student_id_to_remove, course_id_to_remove)

                print(f"Student with ID {student_id_to_remove} removed from course with ID {course_id_to_remove} successfully.")
            else:
                print("Student removal from course canceled.")

        input("\nPress Enter to return to the menu...")


def add_lecturer():
    # Get input for the new lecturer
    lecturer_name = input("Enter the name of the new lecturer: ")
    gender = input("Enter the gender of the new lecturer: ")
    home_address = input("Enter the home address of the new lecturer: ")
    phone_number = input("Enter the phone number of the new lecturer: ")
    email_address = input("Enter the email address of the new lecturer: ")
    department = input("Enter the department of the new lecturer: ")
    hire_date = input("Enter the hire date of the new lecturer: ")

    print(f"Lecturer Name: {lecturer_name}")
    print(f"Gender: {gender}")
    print(f"Home Address: {home_address}")
    print(f"Phone Number: {phone_number}")
    print(f"Email Address: {email_address}")
    print(f"Department: {department}")
    print(f"Hire Date: {hire_date}")

    user_input = input("Proceed adding this new lecturer? (y/n): ").lower()

    if user_input == 'y':
        # Insert the new lecturer into the database
        insert_lecturer(lecturer_name, gender, home_address, phone_number, email_address, department, hire_date)

        print(f"Lecturer '{lecturer_name}' added successfully.")
    else:
        print("Lecturer addition canceled.")

    input("\nPress Enter to return to the menu...")


def assign_course_to_lecturer():
    # Get input for the course and lecturer
    course_id = input("Enter the ID of the course to assign: ")
    lecturer_id = input("Enter the ID of the lecturer to assign the course to: ")

    if not (course_id.isdigit() and lecturer_id.isdigit()):
        print("Invalid input. Please enter valid course and lecturer IDs.")
        return

    course_id = int(course_id)
    lecturer_id = int(lecturer_id)

    # Check if the course and lecturer exist
    if not course_exists(course_id) or not lecturer_exists(lecturer_id):
        print("Invalid course or lecturer ID. Please check the IDs and try again.")
        return

    cursor = conn.cursor()

    # Update the course_data table to assign the course to the lecturer
    cursor.execute("UPDATE course_data SET lecturer_ID = %s WHERE course_ID = %s", (lecturer_id, course_id))
    conn.commit()

    print(f"Course with ID {course_id} assigned to lecturer with ID {lecturer_id} successfully.")


def remove_lecturer():
    # Get input for the lecturer to remove
    lecturer_id_to_remove = input("Enter the ID of the lecturer to remove: ")

    if not lecturer_id_to_remove.isdigit():
        print("Invalid input. Please enter a valid lecturer ID.")
        remove_lecturer()
    else:
        lecturer_id_to_remove = int(lecturer_id_to_remove)

        # Confirm removal with the user
        confirm_removal = input(
            f"Are you sure you want to remove the lecturer with ID {lecturer_id_to_remove}? (y/n): ").lower()

        if confirm_removal == 'y':
            # Remove the lecturer from the database
            delete_lecturer(lecturer_id_to_remove)

            print(f"Lecturer with ID {lecturer_id_to_remove} removed successfully.")
        else:
            print("Lecturer removal canceled.")

        input("\nPress Enter to return to the menu...")
