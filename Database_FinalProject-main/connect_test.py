import mysql.connector

# Replace the placeholders with your MySQL server information
host = "127.0.0.1"
user = "root"
password = "" #Insert database password here.
database = "" #Insert database name here.

# Connect to the MySQL server
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a cursor object
cursor = conn.cursor()

# Execute MySQL queries for student_data
cursor.execute("SELECT * FROM student_data;")
result = cursor.fetchall()

# Display the results
for row in result:
    print(row)

print()

# Execute MySQL queries for lecturer_data
cursor.execute("SELECT * FROM lecturer_data;")
result = cursor.fetchall()

# Display the results
for row in result:
    print(row)

# Close the cursor and connection
cursor.close()

###########################################################################

# Create a cursor object
cursor = conn.cursor()

# Dummy data (replace this with your actual data or fetch it from the database)
students = {
    1: {'name': 'Alice Johnson', 'grades': {}},
    2: {'name': 'Bob Smith', 'grades': {}},
    3: {'name': 'Charlie Brown', 'grades': {}},
    4: {'name': 'Diana Williams', 'grades': {}},
    5: {'name': 'Eva Davis', 'grades': {}},
}

courses = {
    1: {'name': 'Introduction to Programming'},
    2: {'name': 'Circuit Analysis'},
    3: {'name': 'Mechanical Design'},
    4: {'name': 'Quantum Mechanics'},
    5: {'name': 'Calculus I'},
}

# Function to display student grades based on courses
def display_student_grades(student_id):
    # Fetch student information from the database
    cursor.execute("SELECT student_name FROM student_data WHERE student_ID = %s", (student_id,))
    student_info = cursor.fetchone()

    if not student_info:
        print("Student not found.")
        return

    student_name = student_info[0]

    print(f"Student: {student_name}")
    print("\nCourse Grades:")

    # Fetch and display grades for each course
    for course_id in courses.keys():
        cursor.execute("""
            SELECT grade, numerical_grade 
            FROM grades_data 
            WHERE student_ID = %s AND course_ID = %s
        """, (student_id, course_id))

        grade_data = cursor.fetchone()

        course_info = courses[course_id]['name']

        if grade_data:
            print(f"{course_info}: {grade_data[0]} ({grade_data[1]})")
        else:
            print(f"{course_info}: Not available")


# Example: Display grades for student with ID 1
display_student_grades(1)
display_student_grades(2)
display_student_grades(3)
display_student_grades(4)
display_student_grades(5)


# Close the cursor and database connection
cursor.close()
conn.close()