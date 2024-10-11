class Student:
    def __init__(self,Name,ID):
        self.name =Name
        self.id=ID
    def display(self):
        print(f"Name of the student is {self.name} and ID is {self.id}.")

st1=Student("A","3S")
st2=Student("B","5D")
st3=Student("C","2A")
st4=Student("D","9F")
st5=Student("E","8R")

list1=[st1,st2,st3,st4,st5]
# for i in list1:
#     print(i.display())

dict1 =[{"Name":i.name,"ID":i.id} for i in list1]

import pandas as pd
student_database = pd.DataFrame(dict1)
print(student_database.head())

