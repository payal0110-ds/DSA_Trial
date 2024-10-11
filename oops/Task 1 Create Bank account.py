
class Account:
    def __init__(self,Account_Name, Balance):
        self.acc=Account_Name
        self.bal=Balance

    def credit(self):
        try:
            credit_amount=int(input("Add Amout: "))
            if credit_amount<=100000:
                self.bal=self.bal+credit_amount
                print(f"Final Balance is {self.bal}")
            else:
                print("Credit limit exceeds. Maximum limit is 100000.")
        except:
            print("Invalid input. Please enter an integer value.")

    def debit(self):
        try:
            debit_amount=int(input("Debit Amount: "))
            if debit_amount<=self.bal:
                self.bal=self.bal-debit_amount
                print(f"Final Balance is {self.bal}")
            else:
                print("Debit limit exceeds. Debit amount should be less than main balance.")
        except:
            print("Invalid input. Please enter an integer value.")

    def balance(self):
        print(f"The last updated balance is {self.bal}")


acc1=Account("121",10000)
print(acc1.credit(),acc1.debit(),acc1.balance())




