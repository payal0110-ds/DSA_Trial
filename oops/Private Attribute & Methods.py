

class Bank:
    def __init__(self,Account,Balance):
        self.__acc=Account                  # PRIVATE ATTRIBUTE
        self.__bal=Balance                  # PRIVATE ATTRIBUTE
    def __update(self,amount):              # PRIVATE METHOD
        self.__bal+=amount
    def credit(self,amount):
        try:
            if 10000<=amount>0:
                self.__update(amount)
                print(f"Credited amount is {amount}. Final Balance is {self.__bal}.")
            else:
                print("")
        except:
            print("Credit amount should be less than 10000 and more than 0 ")

    def debit(self,amount):
        try:
            if 0<amount<self.__bal:
                self.__update(-amount)
                print(f"Debited amount is {amount}. Final Balance is {self.__bal}.")
            else:
                print("Debited amount is more than saved balance.")
        except:
            print("Enter a valid input.")

c1= Bank("23s",1000)
print(c1.credit(500))
print(c1.debit(200))
print(c1.debit(1400))
#print(c1.credit(asWF))    ''' Shows Error: FIX IT'''