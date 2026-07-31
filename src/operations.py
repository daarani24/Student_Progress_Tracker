def add_student(students):
    roll_no=input("Enter Roll No:")
    for s in students:
        if s[0]==roll_no:
            print("\nRoll Number Already Exists!")
            return
    name=input("Enter Name:")
    dept=input("Enter Department:")
    year=input("Year:")

    s=[roll_no,name,dept,year]
    students.append([roll_no,name,dept,year])

    print("\nStudent Added Successfully!")

def view_students(students):
    if len(students)==0:
        print("\nNo students found")
        return
    for s in students:
        print("\nRoll_No   :",s[0])
        print("Name      :",s[1])
        print("Department:",s[2])
        print("Year      :",s[3])

def update_student(students):
    roll_no=input("Enter Roll No:")
    for s in students:
        if s[0]==roll_no:
            print("student Found")
            s[1]=input("Enter new name:")
            s[2]=input("Enter new department:")
            s[3]=input("Enter new year:")
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
        if s[0]==roll_no:
            students.remove(s)
            print("Student deleted successfully")
            break
    else:
        print("Student not found")

def search_student(students):
    if len(students)==0:
        print("No student is found")
        return
    roll_no=input("Enter Roll No:\n")
    for s in students:
        if s[0]==roll_no:
            print("Roll Number:",s[0])
            print("Name       :",s[1])
            print("Department :",s[2])
            print("Year       :",s[3])
            break
    else:
        print("Student not found")
