import sqlite3

# connect to DB
con = sqlite3.connect("users.db")
cur = con.cursor()

# create users table 
cur.execute("""
            CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL)
            """)
con.commit()

# CRUD OPERATIONS

def create_user():
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    try:
        cur.execute("INSERT INTO users (name,email) VALUES (?,?)", (name,email))
        con.commit()
    except sqlite3.IntegrityError:
        print("Email already exist")

def disp_users():
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    if users:
        for user in users:
            print(f"{user[0]} {user[1]} {user[2]}")
    else:
        print("No user found")

def update_user():
    user_id = input("Enter user ID to update: ")
    new_name = input("New Name: ")
    new_email = input("New Email: ")
    try:
        cur.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (new_name,new_email, user_id))
        if cur.rowcount == 0:
            print("User not found")
        else:
            con.commit()
            print("User Updated")
    except sqlite3.IntegrityError:
        print("Email already exist")

def delete_user():
    user_id = input("enter user Id to be deleted: ")
    cur.execute("DELETE FROM users WHERE id = ?", (user_id))
    if cur.rowcount == 0:
        print("user not found")
    else:
        con.commit()
        print("User Deleted")

def menu():
    print("User....")
    print("1. Add Users")
    print("2. Display Users")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exist")

def main():
    while True:
        menu()
        choice = input("choose a option: ")
        if choice == "1":
            create_user()
        elif choice == "2":
            disp_users()
        elif choice == "3":
            update_user()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            print("BYE")
            break
        else:
            print("Invalid option.... Try again")
    con.close()

if __name__ == "__main__":
    main()