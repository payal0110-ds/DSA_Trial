# Create Class and Object/Instance Attributes
class Student:
    def __init__(self):
        print("Hello Everyone")
st1=Student()
print(st1)


# -------------------------------------------------------
class Student:
    def __init__(self):
        print("Welcome to Brunel.")
    def display(self,name):
        print(f"Name of the styudent is {name}.")

st1=Student()
print(st1.display("Maya"))

#-------------------------------------------------------
class Students:
    University_name="Brunel University"     #Class Attributes: University_name & Location which are common for all instances.
    Location="London"
    def __init__(self,Name,Id,Gender,Marks):  #Object Attributes which are unique for each instnace.
        self.name=Name
        self.id=Id
        self.gender=Gender
        self.marks=Marks

# Create objects
s1=Students("Jai Bali","42A","Male","90%")
s2=Students("Swarna Soman","13F","Female","88%")
s3=Students("Jivika Roy","21A","Female","86%")
s4=Students("Atharv Sant","23S","Male","92%")
s5=Students("Kailash Atwal","19L","Male","82%")

# print(f"Student_1 details are:{s1.name},{s1.id},{s1.gender},{s1.marks},{s1.University_name},{s1.Location}")
# print(f"Student_2 details are:{s2.name},{s2.id},{s2.gender},{s2.marks},{s2.University_name},{s2.Location}")
# print(f"Student_3 details are:{s3.name},{s3.id},{s3.gender},{s3.marks},{s3.University_name},{s3.Location}")
# print(f"Student_4 details are:{s4.name},{s4.id},{s4.gender},{s4.marks},{s4.University_name},{s4.Location}")
# print(f"Student_4 details are:{s5.name},{s5.id},{s5.gender},{s5.marks},{s5.University_name},{s5.Location}")

# Cretae a list and using loop, print all the objects. Optimised code

list_student=[s1,s2,s3,s4,s5]
for i in list1:
    print(f"Details of {i.name} are: {i.id},{i.gender},{i.marks},{i.University_name},{i.Location}")

#-------------------------------------------------------
class Student:
    def __init__(self,Name,Id):
        self.name=Name
        self.id=Id

    def display(self):
        print(f"Hi {self.name}, Your Id will be {self.id}")

st1=Student("Ava","3S")
st2=Student("Manav","2S")
st3=Student("Mavy","6A")
st4=Student("Ruth","7E")
st5=Student("Purav","9R")

list1= [st1,st2,st3,st4,st5]
for i in list1:
    print(i.display())
#-------------------------------------------------------
#Create List for Data values
details=[s1,s2,s3,s4,s5]

#Create Dictionary where key:Variable & values:data values
student_dataset=[{"Name":i.name,"ID":i.id,"Gender":i.gender,"Marks":i.marks,"University Name":i.University_name,"Location":i.Location} for i in details]

import pandas as pd
student_dataset_pd = pd.DataFrame(student_dataset)
print(student_dataset_pd.head())