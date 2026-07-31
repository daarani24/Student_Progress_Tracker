from src.menu import menu
from src.operations import *

students=[]

while True:
    choice=menu()

    if choice=="1":
        add_student(students)
    elif choice=="2":
        view_students(students)
    elif choice=="3":
        update_student(students)
    elif choice=="4":
        delete_student(students)
    elif choice=="5":
        search_student(students)
    elif choice=="6":
        print("Thank You")
        break
    else:
        print('\nInvalid Choice')