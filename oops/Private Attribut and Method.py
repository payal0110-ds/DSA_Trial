''' PRIVATE ATTRIBUTE & METHOD '''
'''
Python doesn't have strict concept of 'Private Attribute & Method', however, we can still achieve 
this concept upto some extent using 'Double Underscore / __' before the attribute and method name.
E.g  __variable
     def __private_function()

- The Private attribute can't be accessible directly by 'Object', however, it can be accessible inside 
'print()' statement.
E.g  def public_method(self):
        print(__variable)
        
- Like how the private method can also be accessible otherway.
>> "dir()" is used to cehck all the methods including private methods of the class.
>> This new method's name is always an underscore, where the class name is mentioned, followed by 
the method name.
>> E.g. ClassName__private()
'''

'''
PRIVATE ATTRIBUTE
'''
# --------------------------------------------------------------------
# class Account:
#     def __init__(self,UserName,Password):
#         self.username=UserName
#         self.__password=Password            # Private Attribute
#
# ob=Account("Maya",298)
# print(ob.__password)                        # Can't be accessible directly.

# --------------------------------------------------------------------
# class Account:
#     def __init__(self,UserName,PassWord):
#         self.username=UserName
#         self.__password=PassWord     #Private Attribute
#         print(f"UserName is {self.username} and Password is {self.__password}.")
#
# ob=Account("George",4728)
# print(ob)                                   # Private Attribute is accesible

# --------------------------------------------------------------------

# class Account:
#     def __init__(self,UserName,Password):
#         self.username=UserName
#         self.__password=Password               # Private Attribute
#     def display(self):
#         print(f"Username is {self.username} and Password is {self.__password}.")
#
# ob=Account("Alicia",383671)
# # print(ob.__password)                            # Not Accessible
# print(ob.display())                               # Accesible

# --------------------------------------------------------------------
# class Account:
#     def __init__(self,UserName,Password):
#         self.username=UserName
#         self.__password=Password                    # Private Attribute
#     def display(self,Balance,Status):
#         self.__balance=Balance
#         self.status=Status
#         print(f"UserId is {self.username}, Password is {self.__password}.")
# ob=Account("Justin",4124123)

# --------------------------------------------------------------------
'''
PRIVATE METHOD
'''
# class Account:
#     def __init__(self,Name,ID):
#         self.name=Name
#         self.id=ID
#         print(f"Name of the customer is {self.name} and ID is {self.id}.")
#     def __password(self,Password):
#         self.password=Password
#         print(f"Customer's password is {self.password}.")
#
# ob=Account("Jacson",298)
# print(ob)
# print(ob.__password())                      # Not Accessible

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

# --------------------------------------------------------------------

class Account:
    def __init__(self,Name):
        self.name=Name
    def __password(self,Password):
        self.password=Password
    def display(self,Balance):
        self.balance=Balance
        print(f"Name of the customer is {self.name}.")
        print(__password("Default"))
        print(f"Account Balance is {self.balance}.")

ob=Account("George")
print(ob.)






