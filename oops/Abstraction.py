'''Simple axample of Abstarction on class Cars where the results are shown to the viewrs without knowing what is the
internal or background processes.'''

class Cars:
    def __init__(self):
        self.acc=bool(int(input("Accelerator, 0 for Flase and 1 for True: ")))
        self.clutch=bool(int(input("Clutch, 0 for Flase and 1 for True: ")))
        self.brk=bool(int(input("Break, 0 for Flase and 1 for True: ")))

    def engine(self):
        print("Accelarator is ",self.acc)
        print("Clutch is ",self.clutch)
        print("Break is ",self.brk)

car1=Cars()
print(car1.engine())

#-------------------------------------------------------------------------

'''Example of Abstraction using class Cars, where the conditions of the engine start or not is hidden to the viewers,
while the result based on the conditions are accesed by the viewers.'''

class Cars:
    def __init__(self):
        self.acc=bool(int(input("Accelerator, 0 for Flase and 1 for True: ")))
        self.clutch=bool(int(input("Clutch, 0 for Flase and 1 for True: ")))
        self.brk=bool(int(input("Break, 0 for Flase and 1 for True: ")))

    def engine(self):
        print(f"Accelerator: {self.acc},Clutch: {self.clutch}, Break: {self.brk}")
        if self.acc and self.clutch and not self.brk == 1:
            print("Car engine starts.")
        elif self.acc and self.brk and not self.clutch ==1:
            print("Car engine breaks.")
        else:
            print("Car engine doesn't start.")

car1=Cars()
print(car1.engine())

#-----------------------------------------------------------------------
# '''Example of Abstraction on class Student
# - The viewrs see the average of the marks along with the name, whereas the calculation for average is abstract or hidden to the viewers.'''
#
# class Students:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def avg(self):
#         total=0
#         for i in self.marks:
#             total+=i
#         average=total/3
#         print(f"Average mark of {self.name} is {average}")
#
# s1=Students("Abc",[2,3,5])
# print(s1.avg())






