# Create a class Student
class Student:
    def __init__(self,Name,Id,Gender,Marks):
        self.name=Name
        self.id=Id
        self.gender=Gender
        self.marks=Marks

#Create objects as students
s1=Student("Jai Bali","42A","Male","90%")
s2=Student("Swarna Soman","13F","Female","88%")
s3=Student("Jivika Roy","21A","Female","86%")
s4=Student("Atharv Sant","23S","Male","92%")
s5=Student("Kailash Atwal","19L","Male","82%")

print(f"Student_1 details are:{s1.name},{s1.id},{s1.gender},{s1.marks}")
print(f"Student_2 details are:{s2.name},{s2.id},{s2.gender},{s2.marks}")
print(f"Student_3 details are:{s3.name},{s3.id},{s3.gender},{s3.marks}")
print(f"Student_4 details are:{s4.name},{s4.id},{s4.gender},{s4.marks}")
print(f"Student_4 details are:{s5.name},{s5.id},{s5.gender},{s5.marks}")
