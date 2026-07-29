from src.menu import menu
from src.operations import add_student,view_students

students=[]

while True:
    choice=menu()

    if choice=="1":
        add_student(students)
    elif choice=="2":
        view_students(students)
    elif choice=="3":
        print("\nThank You")
        break
    else:
        print('\nInvalid Choice')