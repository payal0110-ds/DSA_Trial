class Students:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg(self):
        total=0
        for i in self.marks:
            total+=i
        average=total/3
        print(f"Average mark of {self.name} is {average}")

s1=Students("Abc",[2,3,5])
print(s1.avg())

