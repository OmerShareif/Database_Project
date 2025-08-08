import sqlite3

# create and connect to student database 
con = sqlite3.connect('students.db')
cur = con.cursor()

# create students table
cur.execute("""
                CREATE TABLE students (
                student_id INTEGER PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                date_of_birth TEXT,
                gender TEXT,
                email TEXT UNIQUE,
                phone TEXT,
                course TEXT,
                year INTEGER,
                enrollment_date TEXT
            )        
            """)
con.commit()

# insert student record
def add_student():
    print("----Add New Student----")
    first_name = input("first name: ")
    last_name = input("last name: ")
    dob = input("date of birth (YYYY-MM-DD): ")
    gender = input("gender: ")
    email = input("email: ")
    phone = input("phone: ")
    course = input("course: ")
    year = int(input("year: "))
    enrollment_date = input("enrollment date (YYYY-MM-DD): ")
    cur.execute("""
                    INSERT INTO students (first_name,last_name,date_of_birth,gender,email,phone,course,year,enrollment_date)
                    VALUES (?,?,?,?,?,?,?,?,?)""",
                    (first_name,last_name,dob,gender,email,phone,course,year,enrollment_date)
                )
    con.commit()
    print("Student added successfully")

# retrieve students
def retrieve_students():
    print("---All students---")
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        print()

# Delete s student by ID
def delete_student():
    student_id = input("Enter student Id to be deleted: ")
    cur.execute("DELETE FROM students WHERE student_id = ?",(student_id))
    con.commit()
    print("student Deleted")

# Update student information
def update_student_email():
    student_id = input("enter student id: ")
    new_email = input("enter new email: ")
    cur.execute("UPDATE students SET email = ? WHERE student_id = ?",(new_email,student_id))
    con.commit()
    print("email update successfully")

def menu():
    while True:
        print("---Student Database Menu---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Update Student Email")
        print("5. Exit")

        choice = input("select an option (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            retrieve_students()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            update_student_email()
        elif choice == '5':
            print('Exiting')
            break
        else:
            print('Invalid choice..')

if __name__ == '__main__':
    menu()