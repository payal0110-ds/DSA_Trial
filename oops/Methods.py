class Students:
    def __init__(self, Name, Id, Gender, Marks):
        self.name = Name
        self.id = Id
        self.gender = Gender
        self.marks = Marks

    #     def hello():     Any function/method in class always has at least one argument as 'self' that refers to the object.

    def hello(self):  # Here, the method 'hello' has an argument 'self'
        print("Hello Everyone.")

    def cal1(self):
        print("Welcome", self.name)

s4=Students("Atharv Sant","23S","Male","92%")
s5=Students("Kailash Atwal","19L","Male","82%")
s4.hello()
s4.cal1()
s5.hello()
s5.cal1()

#-------------------------------------------------------------------
'''Claculate grades of students'''
"""Functions without additional ARGUMENTS."""
class Grades:
    def __init__(self,ID,Mathematics,Science,History,Geography,English):
        self.math=Mathematics
        self.sci=Science
        self.his=History
        self.geo=Geography
        self.eng=English
    def total(self):
        return self.math+self.sci+self.his+self.geo+self.eng
    def average(self):
        return (self.math+self.sci+self.his+self.geo+self.eng)/5
    def percentage(self):
        return ((self.math+self.sci+self.his+self.geo+self.eng)/500)*100


s1=Grades("1SD",80,87,77,85,83)
s2=Grades("2TR",91,89,94,89,88)
s3=Grades("2FS",75,65,70,65,74)
s4=Grades("1HS",98,91,83,81,90)

print(f"Total marks of student_1: {s1.total()}, average mark: {s1.average()}, percetange: {s1.percentage()}%.")
print(f"Total marks of student_2: {s2.total()}, average mark: {s2.average()}, percentage: {s2.percentage()}%.")
print(f"Total marks of student_3: {s3.total()}, average mark: {s3.average()}, percentage: {s3.percentage()}%.")
print(f"Total marks of student_4: {s4.total()}, average mark: {s4.average()}, percentage: {s4.percentage()}%.")

#-------------------------------------------------------------------
""" Functions with additional ARGUMENTS"""
class Students:
    def __init__(self,Name,Id):
        self.name=Name
        self.id=Id
        print(f"Hello {self.name}")
    def display(self,Course):                 #Function with argument 'Course'
        self.course=Course
        print(f"Your ID is {self.id} and course is {self.course}.")

st=Students("Avay",241)
print(st.display("Computer Science"))