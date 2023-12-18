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


# Function to fetch student data from the database
def get_student_name(student_name):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student_data WHERE student_name = %s", (student_name,))
    return cursor.fetchone()


# Function to fetch student grades from the database
def get_student_grades(student_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM grades_data WHERE student_ID = %s", (student_id,))
    return cursor.fetchall()


# Function to fetch student data from the database by student ID
def get_student_data_by_id(student_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student_data WHERE student_ID = %s", (student_id,))
    return cursor.fetchone()


# Function to fetch course data from the database by course ID
def get_course_data_by_id(course_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM course_data WHERE course_ID = %s", (course_id,))
    return cursor.fetchone()


def get_students_in_course_with_grades(lecturer_id, course_id):
    cursor = conn.cursor()
    # Replace this query with your actual query to get course_IDs taught by the lecturer
    cursor.execute("""
        SELECT course_ID
        FROM course_data
        WHERE lecturer_ID = %s
    """, (lecturer_id,))

    lecturer_courses = cursor.fetchall()

    if not lecturer_courses:
        return []  # No courses taught by the lecturer

    students_in_course = []

    for course in lecturer_courses:
        current_course_id = course[0]

        if current_course_id == course_id:
            # Fetch student_IDs and grades enrolled in the current course
            cursor.execute("""
                SELECT e.student_ID, g.grade, g.numerical_grade
                FROM enrollment_status e
                LEFT JOIN grades_data g ON e.student_ID = g.student_ID AND e.course_ID = g.course_ID
                WHERE e.course_ID = %s
            """, (course_id,))

            student_grades = cursor.fetchall()

            # Fetch student names using the student_IDs
            for student_grade in student_grades:
                student_id, letter_grade, numerical_grade = student_grade
                cursor.execute("""
                    SELECT student_name
                    FROM student_data
                    WHERE student_ID = %s
                """, (student_id,))

                student_name = cursor.fetchone()
                students_in_course.append((student_id, student_name[0], letter_grade, numerical_grade))

    return students_in_course


def get_lecturer_name(lecturer_name):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lecturer_data WHERE lecturer_name = %s", (lecturer_name,))
    return cursor.fetchone()


def get_lecturer_id(lecturer_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lecturer_data WHERE lecturer_ID = %s", (lecturer_id,))
    return cursor.fetchone()


def get_lecturer_courses(lecturer_id):
    cursor = conn.cursor()
    cursor.execute("SELECT course_ID, course_name FROM course_data WHERE lecturer_ID = %s", (lecturer_id,))
    return cursor.fetchall()


def get_all_courses():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM course_data")
    return cursor.fetchall()


def insert_courses(course_name, course_department, course_credit_hours, course_semester, course_description,
                   lecturer_id):
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(course_ID) FROM course_data")
    max_course_id = cursor.fetchone()[0]

    # Increment the maximum course_ID to get a new course_ID
    new_course_id = max_course_id + 1

    cursor.execute(
        "INSERT INTO course_data (course_ID, course_name, department, credit_hours, "
        "semester, description, lecturer_ID) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (new_course_id, course_name, course_department, course_credit_hours, course_semester, course_description,
         lecturer_id))
    conn.commit()


def delete_courses(course_id_to_delete):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM course_data WHERE course_ID = %s", (course_id_to_delete,))
    conn.commit()


def insert_student(student_name, date_of_birth, gender, home_address, phone_number, email_address, major,
                   year_of_study, admission_date):
    cursor = conn.cursor()

    cursor.execute("SELECT MAX(student_ID) FROM student_data")
    max_student_id = cursor.fetchone()[0]

    # Increment the maximum student_ID to get a new student_ID
    new_student_id = max_student_id + 1

    cursor.execute("""
        INSERT INTO student_data (student_ID, student_name, date_of_birth, gender, home_address, phone_number, 
        email_address, major, year_of_study, admission_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (new_student_id, student_name, date_of_birth, gender, home_address, phone_number, email_address, major,
          year_of_study, admission_date))
    conn.commit()


def delete_student(student_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM student_data WHERE student_ID = %s", (student_id,))
    conn.commit()


def student_exists(student_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student_data WHERE student_ID = %s", (student_id,))
    return cursor.fetchone() is not None


def course_exists(course_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM course_data WHERE course_ID = %s", (course_id,))
    return cursor.fetchone() is not None


def insert_student_to_course(student_id, course_id, semester, year, registration_date, status):
    cursor = conn.cursor()

    # Get the maximum enrollment_ID
    cursor.execute("SELECT MAX(enrollment_ID) FROM enrollment_status")
    max_enrollment_id = cursor.fetchone()[0]

    # Increment the maximum enrollment_ID to get a new enrollment_ID
    new_enrollment_id = max_enrollment_id + 1

    cursor.execute("""
        INSERT INTO enrollment_status (enrollment_ID, student_ID, course_ID, semester, year, registration_date, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (new_enrollment_id, student_id, course_id, semester, year, registration_date, status))

    conn.commit()


def remove_student_from_course(student_id, course_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM enrollment_status WHERE student_ID = %s AND course_ID = %s", (student_id, course_id))
    conn.commit()


def insert_lecturer(lecturer_name, gender, home_address, phone_number, email_address, department, hire_date):
    cursor = conn.cursor()

    cursor.execute("SELECT MAX(lecturer_ID) FROM lecturer_data")
    max_lecturer_id = cursor.fetchone()[0]

    # Increment the maximum student_ID to get a new student_ID
    new_lecturer_id = max_lecturer_id + 1

    cursor.execute("""
        INSERT INTO lecturer_data (lecturer_ID, lecturer_name, gender, home_address, phone_number, 
        email_address, department, hire_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (new_lecturer_id, lecturer_name, gender, home_address, phone_number, email_address, department, hire_date))
    conn.commit()


def lecturer_exists(lecturer_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lecturer_data WHERE lecturer_ID = %s", (lecturer_id,))
    return cursor.fetchone() is not None


def delete_lecturer(lecturer_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM lecturer_data WHERE lecturer_ID = %s", (lecturer_id,))
    conn.commit()


def convert_numerical_to_letter(numerical_grade):
    numerical_grade = float(numerical_grade)

    if 90 <= numerical_grade <= 100:
        return 'A'
    elif 80 <= numerical_grade < 90:
        return 'B'
    elif 70 <= numerical_grade < 80:
        return 'C'
    elif 60 <= numerical_grade < 70:
        return 'D'
    else:
        return 'F'


def update_student_grade(student_id, course_id, new_numerical_grade):
    cursor = conn.cursor()

    cursor = conn.cursor()

    cursor.execute("SELECT MAX(grades_ID) FROM grades_data")
    max_grades_id = cursor.fetchone()[0]

    # Increment the maximum student_ID to get a new student_ID
    new_grades_id = max_grades_id + 1

    # Convert numerical grade to letter grade
    new_letter_grade = convert_numerical_to_letter(new_numerical_grade)

    # Check if a record already exists for the student and course
    cursor.execute("SELECT * FROM grades_data WHERE student_ID = %s AND course_ID = %s", (student_id, course_id))
    existing_record = cursor.fetchone()

    if existing_record:
        # Update the existing record
        cursor.execute(
            "UPDATE grades_data SET numerical_grade = %s, grade = %s WHERE student_ID = %s AND course_ID = %s",
            (new_numerical_grade, new_letter_grade, student_id, course_id)
        )
    else:
        # Insert a new record
        cursor.execute(
            "INSERT INTO grades_data (grades_ID, student_ID, course_ID, grade, numerical_grade) VALUES "
            "(%s, %s, %s, %s, %s)", (new_grades_id, student_id, course_id, new_letter_grade, new_numerical_grade, )
        )

    conn.commit()



