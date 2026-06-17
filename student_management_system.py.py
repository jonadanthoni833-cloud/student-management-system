import sqlite3

conn = sqlite3.connect("my school management system.db")
conn.row_factory = sqlite3.Row

cuser = conn.cursor()

cuser.execute("""
CREATE TABLE IF NOT EXISTS student_info(
              name TEXT NOT NULL,
              age INTEGER NOT NULL,
              grade TEXT)""")
conn.commit()

def add_student():
  name = input("Enter name: ").strip().capitalize()
  age = int(input("Enter age: "))
  grade = input("Enter grade: ").strip()
  cuser.execute("INSERT INTO student_info(name, age, grade) VALUES(?,?,?)", (name, age,grade))
  print(f"Successfully added {name}")
  conn.commit()

def search_student():
  name = input("Enter student name: ").strip().capitalize()
  cuser.execute("SELECT * FROM student_info WHERE name = ?", (name,))
  students = cuser.fetchall()
  if students:
    for student in students:
      print(f"{student['name']} - {student['age']} - {student['grade']}")
  
  else:
    print("Student not found")


def view_students():
  cuser.execute("SELECT * FROM student_info")
  students = cuser.fetchall()
  if students:
    for student in students:
      print(f"{student['name']} - {student['age']} - {student['grade'].upper()}")
  else:
    print("Students not found.")

def delete():
  view_students()
  name = input("Enter student's name to delete: ").strip().capitalize()
  cuser.execute("DELETE FROM student_info WHERE name = ?", (name,))
  conn.commit()
  print(f"{name} deleted successfully")

def menu():
  choices = ["Add student", "Search for a student", "View all students", "Delete a student", "Exit"]
  for choice in enumerate(choices, start= 1):
    print(choice)
  try:
    option = int(input("Enter choice: "))
    if isinstance(option, int):
      pass
    else:
      raise ValueError
  except ValueError:
    print("Enter a numeric value please")
  else:
    return option

while True:
  choice = menu()
  if choice == 1:
    add_student()

  elif choice == 2:
    search_student()

  elif choice == 3:
    view_students()

  elif choice == 4:
    delete()

  elif choice == 5:
    break

  else:
    print("Wrong input..")



