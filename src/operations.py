from src.student import Student

def add_student(students):
    roll_no=input("Enter Roll No:")

    for s in students:
        if s[0]==roll_no:
            print("\nRoll Number Already Exists!")
            return
        
    name=input("Enter Name:")
    dept=input("Enter Department:")
    year=input("Year:")

    s=Student(roll_no,name,dept,year)
    students.append(s)

    print("\nStudent Added Successfully!")

def view_students(students):
    if len(students)==0:
        print("\nNo students found")
        return
    
    for s in students:
        print("\nRoll_No   :",s.roll_no)
        print("Name      :",s.name)
        print("Department:",s.dept)
        print("Year      :",s.year)

def update_student(students):
    if len(students)==0:
        print("\nNo Students Records Available")
        return
    
    roll_no=input("Enter Roll No to Update:")

    for s in students:
        if s.roll_no==roll_no:
            print("\nstudent Found!")
            print("1.Update Name")
            print("2.Update Department")
            print("3.Update Year")
            print("4.Update All")

            c=input("Enter your choice:")

            if c=="1":
                s.name=input("Enter New Name:")
            elif c=="2":
                s.dept=input("Enter New Department:")
            elif c=="3":
                s.year=input("Enter New Year:")
            elif c=="4":
                s.name=input("Enter New Name:")
                s.dept=input("Enter New department:")
                s.year=input("Enter New Year:")
            else:
                print("Invalid choice!")
                return

            print("Student updated successfully")
            break
    else:
        print("Student not found")

def delete_student(students):
    if len(students)==0:
        print("No student detail is found")
        return
    
    roll_no=input("Enter Roll No:")

    for s in students:
        if s.roll_no==roll_no:
            students.remove(s)
            print("Student deleted successfully")
            break
    else:
        print("Student not found")

def search_student(students):
    if len(students)==0:
        print("No student is found")
        return
    
    roll_no=input("Enter Roll No:")

    for s in students:
        if s.roll_no==roll_no:
            print("Roll Number:",s.roll_no)
            print("Name       :",s.name)
            print("Department :",s.dept)
            print("Year       :",s.year)
            break
    else:
        print("Student not found")
