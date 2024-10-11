# Create Class and Object/Instance Attributes
'''Create a simple class without default constructor `'_init`.'''
class Students:
    print("Hello Everyone.")
    print("Welcome to Brunel University.")
    name="Manav"

s1=Students()
print(s1.name)
s2=Students()
print(s2.name)

'''Without any reference, the values of the class are common for all objects.
Here, everytime, same name will be printed for each object as the class Students contains these values and they are
default for each object. 
So, we can create different objects for different values example as for name.'''

class Students:
    def __init__(self,Name):
        print("Hello Everyone.")
        print("Welcome to Brunel University.")
        self.name=Name       #self as default argument that refers to the object being created for the class

s1=Students("Ayush")
print(s1.name)
s2=Students("Manav")
print(s2.name)

''' Here the name is distinct for each object as the self parameter refers to the value being assigned to the object 
created. But the above two sections are common for all the objects as the there is no and called everytime for each 
object parameter to refer for specific object.'''

class Students:
    print("Hello Everyone.")
    print("Welcome to Brunel")
    def __init__(self,Name):
        self.name=Name

s1=Students("Avay")
print(s1.name)
s2=Students("Maya")
print(s2.name)

''' Here the common section is created before the default constructor, hence they'r called once for all the objects.
This is useful when there are some common values/contects need to be called for all objects. '''

#___________________________________________________________________
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

print(f"Student_1 details are:{s1.name},{s1.id},{s1.gender},{s1.marks},{s1.University_name},{s1.Location}")
print(f"Student_2 details are:{s2.name},{s2.id},{s2.gender},{s2.marks},{s2.University_name},{s2.Location}")
print(f"Student_3 details are:{s3.name},{s3.id},{s3.gender},{s3.marks},{s3.University_name},{s3.Location}")
print(f"Student_4 details are:{s4.name},{s4.id},{s4.gender},{s4.marks},{s4.University_name},{s4.Location}")
print(f"Student_4 details are:{s5.name},{s5.id},{s5.gender},{s5.marks},{s5.University_name},{s5.Location}")

'''
METHOD/FUNCTION CALLED BY ANOTHER METHOD/FUNVTION INSIDE THE CALSS 
'''
# --------------------------------------------------------------------
class Calculation:
    def __init__(self,Value1,Value2):
        self.val1=Value1
        self.val2=Value2
    def addition(self):
        return self.val1+self.val2
    def sub(self,Value3):
        self.val3=Value3
        print(self.addition())
        return self.val1-self.val3

ob=Calculation(10,4)
print(ob.sub(3))

# --------------------------------------------------------------------
class Cal:
    def __init__(self,Value1):
        self.val1=Value1
    def addition(self,Value2):
        self.val2 = Value2
        return self.val1+self.val2
    def sub(self,Value3):
        self.val3=Value3
        print(self.addition(5))                 # Default value for Value2
        return self.val1-self.val3

ob=Cal(10)
print(ob.sub(3))