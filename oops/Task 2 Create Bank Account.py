# class Account:
#     def __init__(self,Account_Name,Balance_file):
#         self.acc=Account_Name
#         self.balance
#         self.bal_file= Balance_file
#         self.bal=self.read_balance_from_file()
#
#     def read_balance_from_file(self):
#

import pandas as pd
file=pd.read_csv("/Users/payalparida/Desktop/Balance.csv")
print(file)



# def cal(file):
#
#
#
#
#     try:
#         with open(self.balance_file, 'r') as file:
#             balance = float(file.read())
#         return balance
#     except FileNotFoundError:
#         return 0
#     except ValueError:
#         print("Error: The balance file contains invalid data. Starting with balance 0.")
#         return 0
