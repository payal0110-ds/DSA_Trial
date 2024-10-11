class MathOperation:
    @staticmethod               # Decorator
    def add(a,b):
        return a+b
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def multi(self):
        return self.a*self.b


res1=MathOperation(3,4)
res2=MathOperation(1,4)
print(res1.add(3,4),res1.multi())

#_______________________________________________________

class Students:
    @staticmethod               # Decorator
    def greet():
        print("Hi everyone, welcome to Brunel University.")
    def __init__(self,Name):
        self.name=Name
    def hi(self):
        print(f"Hi {self.name}")

# Create Objects
s1=Students("Manav")
s2=Students("Disha")

print(s1.greet(),s1.hi())

class Math:
    print("Hello World")

s1=Math()
print(s1)