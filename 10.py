import sqlite3
conn = sqlite3.connect("example.db")
cur = conn.cursor()
while True:
    print("\nMenu:")
    print("1. Create Student Table")
    print("2. Delete Student Table")
    print("3. Retrieve Student Data")
    print("4. Exit")
    print("5. Insert Student Data")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        cur.execute("CREATE TABLE IF NOT EXISTS student (roll INTEGER, name TEXT, marks INTEGER)")
        conn.commit()
        print("Student table created.")

    elif choice == '2':
        cur.execute("DROP TABLE IF EXISTS student")
        conn.commit()
        print("Student table deleted.")

    elif choice == '3':

        cur.execute("SELECT * FROM student")
        table_exists = cur.fetchall()

        if table_exists:
            cur.execute("SELECT * FROM student")
            data = cur.fetchall()
            if data:
                print("Student Records:")
                for row in data:
                    print(row)
            else:
                print("Student table is empty.")
        else:
            print("Student table does not exist.")

    elif choice == '4':
        print("Exiting...")
conn.close()
