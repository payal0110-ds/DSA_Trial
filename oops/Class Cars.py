#Creating class for Cars
class Mercedes:
    color="Blue"
    model="Mercedes-Benz"

car1=Mercedes()
print(car1.color)
print(car1.model)

class Mercedes:
    model="Mercedes Benz"
    def __init__(self):
        print("Add a new car to the database.")

car2=Mercedes()
print(car2.model)

# Now let's create a class for Class10 students.
class Class10:
    def __init__(self,full_name):
        self.name=full_name

s1=Class10("Payal")
print(s1.name)

