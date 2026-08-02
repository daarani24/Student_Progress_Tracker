from src.student import Student

def add_student(students):
    roll_no=input("Enter Roll No:")

    for s in students:
        if s.roll_no==roll_no:
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
        print("======== Student Details ========")
        print("\nRoll_No         :",s.roll_no)
        print("Name            :",s.name)
        print("Department      :",s.dept)
        print("Year            :",s.year)

        print("Attendance      :",s.attendance)
        print("Assignment Marks:",s.assignment)
        print("Internal Marks  :",s.internal_marks)

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
    
    roll_no=input("Enter Roll No to Delete:")

    for s in students:
        if s.roll_no==roll_no:
            print("\n===== Student Found =====")
            print("Roll Number :", s.roll_no)
            print("Name        :", s.name)
            print("Department  :", s.department)
            print("Year        :", s.year)

            choice=input("\n Are you sure you want to delete this student? (Y/N):")

            if choice.upper()=='Y':
                students.remove(s)
                print("\nStudent deleted successfully!")
            else:
                print("\nDeletion Cancelled.")
            break
    else:
        print("\nStudent not found")

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

def update_academic_progress(students):
    if len(students)==0:
        print("\nNo Student Records Available.")
        return

    roll_no=input("Enter Roll Number:")

    for s in students:

        if s.roll_no==roll_no:
            print("\n========Update Academic Progress========")
            s.attendance=float(input("Enter Attendance(%):"))
            s.assignment=float(input("Enter Assignment Marks:"))
            s.internal_marks=float(input("Enter Internal marks:"))
            print("\n Academic Progress Updated Successfully!")
            break
    else:
        print("\nStudent Not Found!")

def calculate_performance(s):

    s.average = (s.assignment_marks + s.internal_marks) / 2

    if s.average >= 90:
        s.grade = "O"
    elif s.average >= 80:
        s.grade = "A+"
    elif s.average >= 70:
        s.grade = "A"
    elif s.average >= 60:
        s.grade = "B+"
    elif s.average >= 50:
        s.grade = "B"
    else:
        s.grade = "RA"