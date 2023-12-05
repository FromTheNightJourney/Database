import pandas as pd
from funnyStuff import *
import random
import os
import time
import csv

file_loc = 'studentCSV.csv'

df = pd.read_csv(file_loc)

def introScreen():
    try:
        studentOrLect = str(input("\nAre you a student or lecturer?: "))
        if studentOrLect == "student":
            name = str(input("\nPlease enter your full name: "))
            print("\nWelcome, " + name + "!")
            time.sleep(2)
            return 1
        elif studentOrLect == "lecturer":
            passw = str(input("\nPlease enter the password: "))
            if passw == "E":
                print("\nWelcome, lecturer.")
                time.sleep(2)
                return 2
            else:
                print("\nIncorrect password. Try again.")
                introScreen()
        else:
            print("\nSeems like you made a mistake. Try again.")
            introScreen()
    except ValueError:
        print("\nSeems like you've made a mistake. Try again.")
        introScreen()
    
def studentMenu():
    
    os.system('cls')
    print("Under construction.")

def lecturerMenu():
    
    os.system('cls')
    print("Good " + greeting + ", lecturer. It is currently " + TwoFourHrClock)
    print("\
\nWelcome to the Ouval Academy Database. \n\
For general information and usage, use the word HELP.\n\
To access administrator data, use the word ADMIN and enter the administrator password.\n\
                \n\
--------------------------------------------------------------\n")
    user_action = str(input("Awaiting Input... ")).lower()
    if user_action == "help":
        helpMenu()
    elif user_action == "admin":
        os.system('cls')
        print("no.")    
        time.sleep(2.25)
        lecturerMenu()
    else:
        print("tf")
        time.sleep(2.25)
        lecturerMenu()

def helpMenu():
    
    os.system('cls')
    print("Good " + greeting + ", lecturer. It is currently " + TwoFourHrClock + "\n")
    
    print(">STUDENTS\n\
To see the list of current students.\n")
    
    print(">EDIT\n\
To edit student data.\n")
    
    print(">GACHA\n\
Gambling system if you're ever bored when working.\n")
    
    print(">KENNAN\n\
Scrambles Kennan's name.\n")
    
    print(">GAMEREC\n\
Recommends an excellent game to play in 2023.\n")
    
    print(">MENU\n\
Return to the menu.\n")
    
    whattoDo = str(input("Awaiting user input... ")).lower()
    
    if whattoDo == "students":
        studentList()
    elif whattoDo == "gacha":
        stats = loadStats()
        gachafunc(stats)
    elif whattoDo == "kennan":
        kennan()
    elif whattoDo == "gamerec":
        print("Valorant")
    elif whattoDo == "quit":
        exit()               
    else:
        print("feature under construction/not working rn, try again.")
        helpMenu()
        
def studentList():
    os.system('cls')
    print("Good " + greeting + ", lecturer. It is currently " + TwoFourHrClock + "\n")
    
    print("Welcome to the student list.")
    print("To view a student's data, use their ID.")
    print("To return to the menu screen, use the word MENU.")
    print("------------------------------------------\n")
    
    majorGrouping = df.groupby('major')
    for major, groupDF in majorGrouping:
        print(f"> {major}\n")
        
        # Iterate through students in the group
        for index, student in groupDF.iterrows():
            print(f"[{index}] {student['studentName']}, Year {student['yearofStudy']}")

        print("\n")
    

    userInput = str(input("Awaiting user input... ")).lower()
    if userInput == "menu":
        helpMenu()
    else: 
        try:
            student_id = int(userInput)
            selected_student = df.loc[student_id]
            displayStudentInfo(selected_student)
        except ValueError:
            print("Invalid input. Please enter a valid student ID.")
            studentList()
    
def displayStudentInfo(student):
    os.system('cls')
    print("Good " + greeting + ", lecturer. It is currently " + TwoFourHrClock + "\n")
    
    print("To edit the student information, use the word EDIT.")
    print("To return to the student list, use the word BACK.")
    print("+" + "-"*63 + "+")
    print("|   {:^60}|".format("Student Information"))
    print("+" + "-"*63 + "+")
    print("|   {:<60}|".format(""))
    print("|   {:<60}|".format(f"ID: {student.name}"))
    print("|   {:<60}|".format(f"Name: {student['studentName']}"))
    print("|   {:<60}|".format(f"Date of Birth: {student['dateofBirth']}"))
    print("|   {:<60}|".format(f"Gender: {student['gender']}"))
    print("|   {:<60}|".format(f"Address: {student['address']}"))
    print("|   {:<60}|".format(f"Phone Number: {student['phoneNumber']}"))
    print("|   {:<60}|".format(f"Email Address: {student['emailAddress']}"))
    print("|   {:<60}|".format(f"Major: {student['major']}"))
    print("|   {:<60}|".format(f"Year of Study: {student['yearofStudy']}"))
    print("|   {:<60}|".format(f"Admission Date: {student['admissionDate']}"))
    print("|   {:<60}|".format(f"Additional Teacher's Notes: {student['TeacherNotes']}"))
    print("|   {:<60}|".format(""))
    print("+" + "-"*63 + "+")
    
    user_input = str(input("Awaiting user input: ")).lower()
    if user_input == 'back':
        studentList()
    elif user_input == 'edit':
        editStudentInfo(student)
    elif user_input == 'q':
        exit()
    elif user_input == 'menu':
        helpMenu()
    else:
        print("Invalid input. Returning to the student list.")
        studentList()
        
def editStudentInfo(student):
    os.system('cls')
    print("Edit Student Information\n")
    print("1. Edit Name")
    print("2. Edit Address")
    print("3. Edit Phone Number")
    print("4. Edit Email Address")
    print("5. Edit Teacher's Notes")
    print("6. Back to Student List")
    
    user_input = input("Enter option number: ")
    
    if user_input == '1':
        newName = input("Enter new name: ")
        student['studentName'] = newName
    elif user_input == '2':
        newAddress = input("Enter new address: ")
        student['address'] = newAddress
    elif user_input == '3':
        newPhone = input("Enter new phone number: ")
        student['phoneNumber'] = newPhone
    elif user_input == '4':
        newEmail = input("Enter new email address: ")
        student['emailAddress'] = newEmail
    elif user_input == '5':
        newNote = input("Enter new note: ")
        student['TeacherNotes'] = newNote
    else: 
        print("Invalid input. Returning to the student list.")
        time.sleep(2)
        studentList()

    print("Student information updated successfully.")
    time.sleep(2)
    displayStudentInfo(student)

def gachafunc(stats):
    
    os.system('cls')
    
    options = ['Andrew', 'Kennan', 'Kenneth', 'Adya', 'Cristoval']
    weights = [0.4, 0.25, 0.15, 0.07, 0.03] 
    
    if stats is None or not isinstance(stats, dict):
        stats = {'Andrew': 0, 'Kennan': 0, 'Kenneth': 0, 'Adya': 0, 'Cristoval': 0}

    result = random.choices(options, weights)[0]
    
    stats[result] += 1

    messages = {
        'Andrew': "Oh... you got an Andrew. Quite unfortunate.",
        'Kennan': "You got Kennan! Could've been worse.",
        'Kenneth': "The gacha gods have gifted you Kenneth. Do with that what you will.",
        'Adya': "Surely this is untrue. You have received an Adyatama. That's crazy, ngl.",
        'Cristoval': "A true god among men has descended upon us. Indeed, Cristoval is here."
    }
    
    print("Rolling...")
    time.sleep(1.8)
    print(messages.get(result, "Invalid option."))

    print("If you would like to see the global stats, use the word STATS.")
    play_again = input("Would you like to go again? Use the words YES or NO.").lower()
    if play_again == 'yes':
        gachafunc(stats)
    elif play_again == 'no':
        print("Alright. Just know you were close to winning. Again, if you already won.")
        editStats(stats)
        helpMenu()
    elif play_again == 'stats':
        showStats()
    else:
        print("Invalid input. Returning to the menu.")
        editStats(stats)
        helpMenu()


def editStats(stats):
    existingStats = loadStats()
    
    for name, count in stats.items():
        existingStats[name] += count
    
    file_exists = os.path.isfile('gachaStats.csv')
        
    with open('gachaStats.csv', mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        csv_writer.writerow(['Name', 'Total'])

        for name, count in existingStats.items():
            csv_writer.writerow([name, count])

def loadStats():
    # Load existing statistics from the CSV file
    statistics = {}
    try:
        with open('gachaStats.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                name = row['Name']
                count = int(row['Total'])
                statistics[name] = count
    except FileNotFoundError:
        pass
    return statistics

def showStats():
    os.system('cls')
    try:
        with open('gachaStats.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            
            # Skip the header
            next(csv_reader, None)

            # Iterate through the rows and display the data
            for row in csv_reader:
                name, total = row
                print(f"{name}: {total}")
                
            input("Press Enter to continue.")
            helpMenu()
                
    except FileNotFoundError:
        print("The global stats cannot be found at the moment.")
        time.sleep(1)
        helpMenu()
        
def kennan():
    os.system('cls')
    kennan = list("kennan")
    random.shuffle(kennan)
    finalProduct = ''.join(kennan)
    print("\n" + finalProduct)
    if finalProduct == "kennan":
        print("Huh. You managed to get the words in the right order. Huh.\n")
    else:
        print("That's it. What did you expect?\n")
    print("Returning to the Menu.")
    time.sleep(1.4)
    helpMenu()
    print("Returning to the Menu.")
    time.sleep(1.4)
    helpMenu()
    
