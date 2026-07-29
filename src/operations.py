def add_student(students):
    roll_no=input("Enter Roll No:")
    name=input("Enter Name:")
    dept=input("Enter Department:")
    year=input("Year:")

    students.append([roll_no,name,dept,year])

    print("\nStudent Added Successfully!")

def view_students(students):
    if len(students)==0:
        print("\nNo students found")
        return
    for s in students:
        print("Roll_No:",s[0])
        print("Name:",s[1])
        print("Department:",s[2])
        print("Year:",s[3])