from students_function import *
from lecturer_function import *
from admin_function import *
from current_time import *
import os
import time


def intro_screen():
    os.system('cls')
    try:
        print("Welcome to the Ouvahl Academy Database\n")
        print("Happy " + dayNow + "\n")
        user_role = str(input("Are you a student or a lecturer?: ")).lower()
        if user_role == "student":
            name = str(input("\nPlease enter your full name: "))
            capitalizeName = name.title()
            student_data = get_student_name(name)

            if student_data:
                print("\nWelcome, " + capitalizeName + "!")
                time.sleep(2)
                student_menu(student_data[0])  # Return the student ID
            else:
                print("\nStudent not found. Please check your name and try again.")
                input("Press ENTER to continue...")
                intro_screen()

        elif user_role == "lecturer":
            lecturer_name = str(input("\nPlease enter your full name: "))
            lecturer_data = get_lecturer_name(lecturer_name)
            first_name = lecturer_data[1].split()[0]

            if lecturer_data:
                lecturer_id = str(input("\nPlease enter your Lecturer ID as a password: "))
                if lecturer_id == str(lecturer_data[0]):  # Assuming lecturer ID is stored as a string
                    print(f"Good {greeting}, {first_name}. Great to have you here.")
                    time.sleep(2)
                    lecturer_menu(lecturer_data[0],first_name)  # Pass lecturer_ID to lecturer_menu
                else:
                    print("\nIncorrect password. Try again.")
                    input("Press ENTER to continue...")
                    intro_screen()
            else:
                print("\nLecturer not found. Please check your name and try again.")
                input("Press ENTER to continue...")
                intro_screen()

        elif user_role == "ADMIN":
            # admin_password = input("\nEnter the admin password: ")  # You can replace this with your actual admin password logic
            #
            # # Check if the admin password is correct
            # if admin_password == "your_actual_admin_password":
            admin_menu()
            # else:
            #     print("Incorrect admin password. Returning to the main menu.")
            #     time.sleep(2)
            #     intro_screen()

        else:
            print("\nSeems like you made a mistake. Try again.")
            input("Press ENTER to continue...")
            intro_screen()

    except ValueError:
        print("\nSeems like you've made a mistake. Try again.")
        input("Press ENTER to continue...")
        intro_screen()
    
def student_menu(student_id):
    student_data = get_student_data_by_id(student_id)
    while True:
        os.system('cls')
        print("\n\
Good " + greeting + f", {student_data[1]}! Welcome to the Ouval Academy Database. \n\
For general information and usage, use the word HELP.\n\
                \n\
--------------------------------------------------------------\n")
        # print("1. Check Grades\n")
        # print("2. Check Information\n")
        # print("3. Quit")
        print(">GRADES\n\
View the grades of your courses.\n")
        print(">INFO\n\
View your personal information within the Academy's database.\n")
        print(">QUIT\n\
Quit the application.\n")

        choice = input("Awaiting user input...").lower()

        if choice == "grades":
            display_student_grades_from_db(student_id)
        elif choice == "info":
            display_student_info(student_id)
        elif choice == "quit":
            break
        else:
            print("Invalid choice. Please enter the word corresponding to the action.")
            input("Press ENTER to continue...")


def lecturer_menu(lecturer_id, lecturer_name):
    first_name = lecturer_name.split()[0]
    while True:
        os.system('cls')
        print(f"Good {greeting}, {first_name}. It is currently " + TwoFourHrClock)
        print("\
\nWelcome to the Ouval Academy Database. \n\
For general information and usage, use the word HELP.\n\
                \n\
--------------------------------------------------------------\n")
        print(">VIEW")
        print("View the courses that you currently teach, along with its students.\n")
        print(">EDIT")
        print("Edit information regarding the students in a course.\n")
        print("QUIT")
        print("Quit the application.\n")
        
        # print("1. View Courses\n")
        # print("2. Edit Mode\n")
        # print("3. Quit\n")
        
        print("Enter your choice...")
        user_action = input("Awaiting user input: ").lower()

        if user_action == "view":
            view_courses(lecturer_id)
        elif user_action == "edit":
            edit_mode(lecturer_id)
        elif user_action == "quit":
            break
        else:
            print("Invalid choice. Please enter a word.")
            input("Press ENTER to continue...")


def admin_menu():
    while True:
        os.system('cls')
        print("Admin Menu:")
        print("1. Add Course")
        print("2. Delete Course")
        print("3. Add Student")
        print("4. Remove Student")
        print("5. Add Student to Course")
        print("6. Delete Student from Course")
        print("7. Add Lecturer")
        print("8. Assign Course to Lecturer")
        print("9. Remove Lecturer")
        print("10. Quit")

        admin_action = input("Enter your choice (1-9): ").lower()

        if admin_action == "1":
            add_course()
        elif admin_action == "2":
            delete_course()
        elif admin_action == "3":
            add_student()
        elif admin_action == "4":
            remove_student()
        elif admin_action == "5":
            add_student_to_course()
        elif admin_action == "6":
            delete_student_from_course()
        elif admin_action == "7":
            add_lecturer()
        elif admin_action == "8":
            assign_course_to_lecturer()
        elif admin_action == "9":
            remove_lecturer()
        elif admin_action == "10":
            break
        else:
            print("Invalid choice. Please enter a valid option (1-10).")
            input("Press ENTER to continue...")

