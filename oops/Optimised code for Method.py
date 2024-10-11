# Write an optimised code to claculate the average marks for 5 subjects for the students.
class Students:
    def __init__(self,Name,Marks):
        self.name=Name
        self.marks=Marks                # Considering 'Marks as a list of 3 subjects' marks.

    def average(self):
        total=0
        for i in self.marks:            # Create a loop to claculate the sum of all the marks.
            total+=i
        print(f"Average mark of {self.name} is {total/5}")

# Create objects
s1=Students("Manav",[79,86,85,90,78])
s2=Students("Jivika",[97,90,89,88,92])
s3=Students("Raj",[78,88,90,76,85])
s4=Students("Megha",[60,68,75,70,65])
s5=Students("Jay",[95,90,87,85,83])

# Create a list of the objects to print together using a loop
student_list=[s1,s2,s3,s4,s5]

for i in student_list:
    print(i.average())

# -------------------------------------------------------------------
# class Students1:
#     def __init__(self,ID,Marks):     # Considering 'Marks as a list of 3 subjects' marks.
#         self.id=ID
#         self.marks=Marks
#     def  average(self):
#         sum=0
#         for i in self.marks:
#             sum = sum+i
#         print(f"The average marks of {self.id} is {sum/3}.")
#
# s1=Students1("1D",[80,83,79])
# s2=Students1("2F",[90,85,88])
# s3=Students1("1T",[68,78,65])
#
# list2=[s1,s2,s3]
# for i in list2:
#     print(i.average())