'''Various Cases: 16 Cases All Total'''

"""PARENT CLASS"""
'''
1. Default + NO Arg               2. Default + Arg
3. Additional + NO Arg            4. Additional + Arg
'''
"""CHILD CLASS"""
'''
a. Default + NO Arg               b. Default + Arg
c. Additional + NO Arg            d. Additional + Arg
'''

"""1.a: Default(No Arg) + Default(No Arg)"""
# class Student:
#     def __init__(self):
#         print("Hello Evreyone.")
# class Child(Student):
#     def __init__(self):
#         Student.__init__(self)
#         print("Welcome to Brunel.")
#
# st=Child()
# print(st)

'''
Hello Evreyone.
Welcome to Brunel.
'''
#____________________________________________________________________________________

"""1.b: Default(No Arg) + Default(Arg) """
# class Student:
#     def __init__(self):
#         print("Welcome everyone.")
#
# class Child:
#     def __init__(self,Name,Id):
#         Student.__init__(self)
#         self.name=Name
#         self.id=Id
#         print(f"Hi {self.name}, your ID is {self.id}.")
#
# st=Child("Ritik",72)
# print(st)

'''
Welcome everyone.
Hi Ritik, your ID is 72.
'''
#____________________________________________________________________________________

"""1.c: Default(No Arg) + Additional (No Arg)"""
# class Student:
#     def __init__(self):
#         print("Hii everyone.")
#
# class Child(Student):
#     def __init__(self):
#         Student.__init__(self)
#     def display(self):
#         print("Welcome to Brunel.")
#
# st=Child()
# print(st.display())

'''
Hii everyone.
Welcome to Brunel.
'''
#____________________________________________________________________________________

"""1.d: Default(No Arg) + Additional(Arg)"""
# class Student:
#     def __init__(self):
#         print("Welcome to Brunel.")
#
# class Child(Student):
#     def __init__(self):
#         Student.__init__(self)
#     def display(self,Name,ID):
#         self.name=Name
#         self.id=ID
#         print(f"Hi {self.name}, your ID is {self.id}.")
#
# st=Child()
# print(st.display("George",141))

'''
Welcome to Brunel.
Hi George, your ID is 141.
'''
#____________________________________________________________________________________

"""2.a: Default(Arg) + Default(No Arg)"""

# class Student:
#     def __init__(self,Name,ID):
#         self.name=Name
#         self.id=ID
#         print(f"Hi {self.name}, your ID is {self.id}.")
#
# class Child(Student):
#     def __init__(self,arg1,arg2):             #Same Arguments for Child constructor like Parent constructor inside Child class
#         Student.__init__(self,arg1,arg2)
#         print("Welcome to Brunel.")
#
# st=Child("Manav",215)
# print(st)

#-----------------------------------------------------------------
'''Another Way using SUPER FUNCTION'''
# class Student:
#     def __init__(self,Name,ID):
#         self.name=Name
#         self.id=ID
#         print(f"Hi {self.name}, your ID is {self.id}.")
#
# class Child(Student):
#     def __init__(self,Name,ID):             #Same Arguments for Child constructor like Parent constructor inside Child class
#         super().__init__(Name, ID)          # Super() indicates the Parent/super class
#         print("Welcome to Brunel.")
#
# st=Child("Manav",211)
# print(st)

'''
Hi Manav, your ID is 211.
Welcome to Brunel.
'''
#____________________________________________________________________________________

"""2.b: Default(Arg) + Default(Arg)"""
# class Student:
#     def __init__(self,Name,ID):
#         self.name=Name
#         self.id=ID
#         print(f"Hi {self.name}, your ID is {self.id}.")
#
# class Child:
#     def __init__(self,Name,ID,Course):
#         Student.__init__(self,Name,ID)
#         self.course=Course
#         print(f"{self.name}, your course will be {self.course}")
#
# st=Child("Max",247,"Data Science.")
# print(st)

'''
Hi Max, your ID is 247.
Max, your course will be Data Science.
'''
#____________________________________________________________________________________

"""2.c: Default(Arg) + Additional (No Arg)"""
# class Student:
#     def __init__(self,Name,Id):
#         self.name=Name
#         self.id=Id
#         print(f"Name of the student is {self.name} and ID is {self.id}.")
#
# class Child(Student):
#     def __init__(self,Name,Id,Course):
#         Student.__init__(self,Name,Id)
#         self.course=Course
#     def stream(self):
#         print(f"{self.name} course is {self.course}.")
#
# st=Child("Maria",133,"Artificial Intellegence")
# print(st,st.stream())

'''
Name of the student is Maria and ID is 133.
Maria course is Artificial Intellegence.
'''
#____________________________________________________________________________________

"""2.d: Default(Arg) + Additional(Arg)"""
# class Student:
#     def __init__(self,Name,Id):
#         self.name=Name
#         self.id=Id
#         print(f"Name of the student is {self.name} and ID is {self.id}.")
#
# class Child(Student):
#     def stream(self,Course):
#         self.course=Course
#         print(f"{self.name}'s course is {self.course}.")
#
# st=Child("Maria",133)
# print(st,st.stream("Artificial Intellegence"))

'''
Name of the student is Maria and ID is 133.
Maria's course is Artificial Intellegence.
'''
#____________________________________________________________________________________

"""3.a: Additional(No Arg) + Default(No Arg)"""
# class Student:
#     def display(self):
#         print("Hello Everyone.")
#
# class Child(Student):
#     def __init__(self):
#         Student.display(self)
#         print("Welcome to Brunel.")
#
# st=Child()
# print(st)

'''
Hello Everyone.
Welcome to Brunel.
'''
#____________________________________________________________________________________

"""3.b: Additional(No Arg) + Default(Arg)"""
# class Student:
#     def display(self):
#         print("Welcome to Brunel.")
#
# class Child(Student):
#     def __init__(self,Name,ID):
#         Student.display(self)
#         self.name=Name
#         self.id=ID
#         print(f"Name of the student is {self.name} and ID is {self.id}.")
#
# st=Child("Raya",241)
# print(st)

'''
Welcome to Brunel.
Name of the student is Raya and ID is 241
'''
#____________________________________________________________________________________

"""3.c: Additional(No Arg) + Additional(No Arg)"""

# class Student:
#     def hello(self):
#         print("Hello Everyone")
#
# class Child(Student):
#     def welcome(self):
#         print("Welcome to Brunel.")
#
# st=Child()
# print(st.hello(),st.welcome())

'''
Hello Everyone
Welcome to Brunel.
'''
#____________________________________________________________________________________

"""3.d: Additional(No Arg) + Additional(Arg)"""
# class Student:
#     def display(self):
#         print("Hello everyone.")
#
# class Child(Student):
#     def name(self,Name):
#         self.name=Name
#         print(f"Name of the student is {self.name}.")
#
# st=Child()
# print(st.display(),st.name("Ana"))

'''
Hello everyone.
Name of the student is Ana.
'''
#____________________________________________________________________________________

"""4.a: Additional(Arg) + Default(No Arg)"""
# class Student:
#     def name(self,Name):
#         self.name=Name
#         print(f"Name of the student is {self.name}.")
#
# class Child(Student):
#     def __init__(self):
#         print("Welcome to Brunel.")
#
# st=Child()
# print(st.name("Maya"))

'''
Welcome to Brunel.
Name of the student is Maya.
'''
#-----------------------------------------------------------------
'''Another Way using SUPER FUNCTION'''
# class Student:
#     def name(self,Name):
#         self.name=Name
#         print(f"Name of the student is {self.name}.")
#
# class Child(Student):
#     def __init__(self,Name):                 #Child:Constructor with Argument that refers to the Parent class constructor
#         Student.name(self,Name)
#         print(f"{self.name}, Welcome to Brunel.")
#
# st=Child("Alex")
# print(st)

'''
Name of the student is Alex.
Alex, Welcome to Brunel.
'''
#____________________________________________________________________________________

"""4.b: Additional(Arg) + Default(Arg)"""
# class Student:
#     def display(self,Name):
#         self.name=Name
#         print(f"Name of the student is {self.name}.")
#
# class Child(Student):
#     def __init__(self,Name,Course):
#         self.course=Course
#         Student.display(self,Name)
#         print(f"{self.name} is enrolled for {self.course}.")
#
# st=Child("Justin","Computer Science")
# print(st)

'''
Name of the student is Justin.
Justin is enrolled for Computer Science.
'''
#-----------------------------------------------------------------
'''Another Approach'''
# class Student:
#     def display(self,Name):
#         self.name=Name
#         print(f"Name of the student is {self.name}.")
#
# class Child(Student):
#     def __init__(self,Course):
#         self.course=Course
#         print(f"The student is enrolled for {self.course}.")
#
# st=Child("Computer Science")
# print(st.display("Joe"))

'''
The student is enrolled for Computer Science.
Name of the student is Joe.
'''
#____________________________________________________________________________________
"""4.d: Additional(Arg) + Additional(No Arg)"""
# class Student:
#     def details(self,Name):
#         self.name=Name
#         print(f"Name of the student is {self.name}.")
#
# class Child(Student):
#     def display(self):
#         print("Welcome to Brunel.")
#
# st=Child()
# print(st.details("Jackson"),st.display())

'''
Name of the student is Jackson.
Welcome to Brunel.
'''
#-----------------------------------------------------------------
'''Another Approach'''
# class Student:
#     def details(self,Name):
#         self.name=Name
#         print(f"Name of the student is {self.name}.")
#
# class Child(Student):
#     def display(self,Name):
#         Student.details(self, Name)
#         print(f"Hi {self.name}, Welcome to Brunel.")
#
# st=Child()
# print(st.display("Jackson"))

'''
Name of the student is Jackson.
Hi Jackson, Welcome to Brunel.
'''
#____________________________________________________________________________________
"""4.c: Additional(Arg) + Additional(Arg)"""

# class Student:
#     def display(self,Name):
#         self.name=Name
#         print(f"Name of the student is {self.name}.")
#
# class Child(Student):
#     def details(self,Name,Id):
#         self.id=Id
#         Student.display(self,Name)
#         print(f"ID of {self.name} is {self.id}.")
#
# st=Child()
# print(st.details("Lilly",231))

'''
Name of the student is Lilly.
ID of Lilly is 231.
'''
#-----------------------------------------------------------------
'''Another Approach'''

# class Student:
#     def display(self,Name):
#         self.name=Name
#         print(f"Name of the stiudent is {self.name}.")
#
# class Child(Student):
#     def details(self,Id):
#         self.id=Id
#         print(f"Student's ID is {self.id}.")
#
# st=Child()
# print(st.display("Joe"),st.details(241))

'''
Name of the stiudent is Joe.
Student's ID is 241.
'''










