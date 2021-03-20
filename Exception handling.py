# ATM project
# define Python user-defined exceptions
"""
Table of Contents
Enter Pin
1.check pin (4times allowed to enter again)
choice of option(s):
1.Deposit
2.withdrawal
3.Mini_statement
4.Exit
"""

from project.error import *
import os


class Account:
    def __init__(self):
        pass


class Atm(Error):
    def __init__(self):
        self.__pin_number = 1234
        self.balance = 25000
        self.my_account()

    def my_account(self):
        try:
            file = open("mini-smt.txt", 'w+')
            file.seek(0)  # sets  point at the beginning of the file
            file.truncate()  # Clear previous content
            mini = ("your initial balance is {} \n".format(self.balance))
            file.write(mini)
        finally:
            file.close()

    # getter and setter function

    def setpin(self, pin_number):
        if username == "Padmaja":
            self.__pin_number = pin_number
        else:
            print('Not allowed to change pin, contact bank')
            self.continue_banking()

    def getpin(self):
        return self.__pin_number

    def log_in(self):
        tries = 0
        while tries < 4:
            pin_entered = int(input('Please Enter Your 4 Digit Pin: '))
            if self.check_pin(pin_entered):
                print("Pin accepted!")
                return True
            else:
                print("Invalid pin")
                tries += 1
        print("To many incorrect tries. Could not log in")
        return self.exit_atm()

    def check_pin(self,pin_entered):
        count = 0
        value = pin_entered
        while value > 0:
            value //= 10
            count += 1
        try:
            if count == 4 and self.__pin_number == pin_entered:
                self.choice()
            elif count > 4 and count < 4:
                raise Error()
            elif self.__pin_number != pin_entered:
                raise EnteredValueError()
            else:
                raise SomethingWrong()
                return False
        except EnteredValueError as ev:
            print(ev)
            self.exit_atm()
        except SomethingWrong as es:
            print(es)
            self.exit_atm()
        except Error as er:
            print(er)
            self.exit_atm()
        else:
            print(":::::::::::::: Thank you for using ATM! ::::::::::::::")

    def change_pin(self):
        value = input("Do you want to change? Y/N : ")
        try:
            if value.upper() == 'Y':
                change_pin = int(input("Enter the new number : "))
                self.setpin(change_pin)
                print("Your Pin has successfully changed")
            else :
                print("Your Pin has not changed")
        finally:
            self.continue_banking()

    def add_amount(self):
        amount_to_add = int(input("Enter the amount :"))
        amount = amount_to_add
        if (amount % 100) == 0 and amount < 25000:
            total = self.balance + amount
            self.balance = total
            self.account_change(amount, total, 'credited')
        else:
            if (amount % 100) != 0:
                raise Error
            else:
                raise EnteredValueError

    def account_change(self, amount, total, action):
        print("{} transaction is successful".format(username))
        print("{} is credited to your account, your new balance is {} ".format(amount, total))
        try:
            file = open("mini-smt.txt", 'a')
            update = ("Amount {} {} to your account. New balance is {} \n".format(amount, action, total))
            file.writelines(update)
        finally:
            file.close()
            self.continue_banking()

    def continue_banking(self):
            option1 = input("Do you want to continue banking[Y/N] : ")
            if option1.lower() == 'y':
                self.choice()
            else :
                self.exit_atm()

    def take_amount(self):
        withdraw = int(input("Enter the amount : "))
        amount = withdraw
        if (amount % 100) == 0 and amount < 25000:
            total = self.balance - amount
            self.balance = total
            self.account_change(amount, total, 'debited')
        else:
            if (amount % 100) != 0:
                raise Error
            else:
                raise EnteredValueError

    def mini_statement(self, amount):
        try:
            file = open("mini-smt.txt",'r')
            data = file.read()
            print(data)
        finally:
            file.close()
            self.continue_banking()

    def exit_atm(self):
        print("thank you")

    def choice(self):
        print("Choose your option:")
        print(" Deposit -'D'\n Withdrawal - 'W'\n Mini-statement - 'M'\n Change-pin  - 'C'\n Exit - 'X'\n")
        option = input("Enter your choice : ")
        result = option.upper()
        try:
            if result == 'D':
                print('Deposit')
                self.add_amount()
            elif result == 'W':
                print('withdrawal')
                self.take_amount()
            elif result == 'M':
                print('Mini-statement')
                self.mini_statement(self.balance)
            elif result == 'X':
                print("thank you")
            elif result == 'C':
                print("change pin")
                self.change_pin()
        except EnteredValueError as ve:
            if result == ' ':
                raise EnteredValueError
            else:
                self.choice()


print(":::::::::::::: welcome to ATM! ::::::::::::::")
username = input("Enter user name :  ")
atm = Atm()
atm.log_in()
