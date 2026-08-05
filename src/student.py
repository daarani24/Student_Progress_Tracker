class Student:
    def __init__(self,roll_no,name,dept,year):
        self._roll_no=roll_no
        self._name=name
        self._dept=dept
        self._year=year

        self._attendance=0.0
        self._assignment=0.0
        self._internal_marks=0.0

        self._average=0.0
        self._grade=""     

    def get_roll_no(self):
        return self._roll_no
    def get_name(self):
        return self._name
    def get_dept(self):
        return self._dept
    def get_year(self):
        return self._year

    def get_attendance(self):
        return self._attendance
    def get_assignment(self):
        return self._assignment
    def get_internal_marks(self):
        return self._internal_marks

    def get_average(self):
        return self._average
    def get_grade(self):
        return self._grade
    
    def set_name(self,name):
        self._name=name
    def set_dept(self,dept):
        self._dept=dept
    def set_year(self,year):
        self._year=year

    def set_attendance(self,attendance):
        self._attendance=attendance
    def set_assignment(self,marks):
        self._assignment=marks
    def set_internal_marks(self,marks):
        self._internal_marks=marks

    def calculate_performance(self):

        self._average = (self._assignment + self._internal_marks) / 2

        if self._average >= 90:
            self._grade = "O"
        elif self._average >= 80:
            self._grade = "A+"
        elif self._average >= 70:
            self._grade = "A"
        elif self._average >= 60:
            self._grade = "B+"
        elif self._average >= 50:
            self._grade = "B"
        else:
            self._grade = "RA"

    def update_academic_progress(self, attendance, assignment, internal):
        self.set_attendance(attendance)
        self.set_assignment(assignment)
        self.set_internal_marks(internal)
        self.calculate_performance()
