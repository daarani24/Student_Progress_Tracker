class Student:
    def __init__(self,roll_no,name,dept,year):
        self.roll_no=roll_no
        self.name=name
        self.dept=dept
        self.year=year

        self.attendance=0
        self.assignment=0
        self.internal_marks=0

        self.average=0
        self.grade=""        