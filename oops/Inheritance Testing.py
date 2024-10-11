# ''' MULTIPLE INHERITANCE'''
# class St1:
#     def __init__(self,Name):
#         self.name=Name
#         print("Welcome to Brunel.")
#     def town(self,City):
#         self.city=City
#         print(f"{self.name} is from {self.city}.")
#
# class St2:
#     def __init__(self,Id):
#         self.id=Id
#     def course(self,Course):
#         self.course=Course
#
# class Child(St1,St2):
#     def __init__(self,Name,ID,Course):
#         St1.__init__(self,Name)
#         St2.__init__(self,ID)
#         St2.course(self,Course)
#         print(f"Name of the student is {self.name}, and Id is {self.id} and course is {self.course}.")
#
# st=Child("Manyata",33,"Data Science")
# print(st)
# st1=St1("Manyata")
# print(st1.town("Delhi"))

''' Here, the child class 'Child' does not inheritate the characterstics 'town' form the parent class 'St1' as it does 
 not call 'city' argument in its default constructor's argument.
 So we can't access the costructor 'town' in the Child class.
 But we can access the constructor 'town' in the Parent class by creating another object for the parent class.'''
#--------------------------------------------------------------------------------
''' TREE STRUCTURE'''
# class StP1:
#     def __init__(self,Name):
#         self.name=Name
# class StP2:
#     def __init__(self,City):
#         self.city=City
#
# class StP3:
#     def __init__(self,Age):
#         self.age=Age
#
# class ChP1(StP1,StP2):
#     def __init__(self,Name,City,Id):
#         StP1.__init__(self,Name)
#         StP2.__init__(self,City)
#         self.id=Id
#
# class ChP2(StP3):
#     def __init__(self,Age,Course):
#         StP3.__init__(self,Age)
#         self.course=Course
#
# class Child(ChP1,ChP2):
#     def __init__(self,Name,City,Id,Age,Course):
#         ChP1.__init__(self,Name,City,Id)
#         ChP2.__init__(self,Age,Course)
#         print("Welcome to Brunel.")
#         print(f"Name of the student is {self.name}, ID is {self.id}, course is {self.course}.")
#         print(f"{self.name}'s age is {self.age} and belongs to {self.city}.")
#
# st1=Child("Avay","Bangalore",47,27,"Data Science")
# print(st1)
''' 3 Parent classes 'StP1', 'StP2' & 'StP3', 2 Child classes are derived as 'ChP1' from 'StP1', 'StP2' & 'ChP2' from 'StP3'.
Then 'Child' class is derived from 'ChP1' & 'ChP2' as parent classes.  
'''
#--------------------------------------------------------------------------------
#
# class StP1:
#     def __init__(self,Name,Id):
#         self.name=Name
#         self.id=Id
#
# class StP2:
#     def __init__(self,Course):
#         self.course=Course
#
# class StP3:
#     def __init__(self,Grade):
#         self.grade=Grade
#
# class ChP1(StP1,StP2):
#     def __init__(self,Name,Id,Course,Gender):
#         StP1.__init__(self,Name,Id)
#         StP2.__init__(self,Course)
#         self.gender=Gender
#
# class ChP2(StP1,StP3):
#     def __init__(self,Name,Id,Grade,City):
#         StP1.__init__(self,Name,Id)
#         StP3.__init__(self,Grade)
#         self.city=City
#
# class Child(ChP1,ChP2):
#     def __init__(self,Name,Id,Name1,Id1,Course,Grade,Gender,City):
#         ChP1.__init__(self,Name,Id,Course,Gender)
#         ChP2.__init__(self,Name1,Id1,Grade,City)
#         print(f"Name of the student is {self.name} and ID is {self.id}.")
#         print(f"{self.name}'s course is {self.course} and grade is {self.grade}.")
#         print(f"{self.name}'s gender is {self.gender} and belongs to {self.city}.")
#
# st1=Child("Ruby",89,"Ruby",89,"Data Science", "A", "Female","Bangalore")
# print(st1)

''' 3 Parent classes 'StP1', 'StP2' & 'StP3', 2 Child classes are derived as 'ChP1' from 'StP1', 'StP2' & 'ChP2' from 
'StP1' & 'StP3'.
- 'StP1' has 2 arguments and child classes must mention all the arguments of the default construcor when they inherit
the parent class.
(SO it's same as the above snipet, and there is no point to call 'StP1' arguments twice when its one child class inherits
all the ARGUMENTS from the DEFAULT CONSTRUCTOR.
Then 'Child' class is derived from 'ChP1' & 'ChP2' as parent classes.  
'''

#--------------------------------------------------------------------------------

class StP1:
    def nm(self,Name):
        self.name=Name
    def crs(self,Course):
        self.course=Course

class StP2:
    def __init__(self,ID):
        self.id=ID

class StP3:
    def __init__(self,Grade):
        self.grade=Grade

class ChP1(StP1,StP2):
    def __init__(self,Name,Id,Age):
        StP1.nm(self,Name)
        StP2.__init__(self,Id)
        self.age=Age

class ChP2(StP1,StP3):
    def __init__(self,Course,Grade,City):
        StP1.crs(self,Course)
        StP3.__init__(self,Grade)
        self.city=City

class Child(ChP1,ChP2):
    def __init__(self,Name,ID,Age,Course,Grade,City):
        ChP1.__init__(self,Name,ID,Age)
        ChP2.__init__(self,Course,Grade,City)
        print(f"Name of the student is {self.name} and ID is {self.id}.")
        print(f"{self.name}'s course is {self.course} and garde is {self.grade}.")
        print(f"{self.name}'s age is {self.age} and belongs to {self.city}.")

st= Child("Nitesh",53,24,"Data Science","B","Delhi")
print(st)

''' Create multiple different constructors in Parents class which are inherited by multiple child classes differently.'''
