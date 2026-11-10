# #bank account==owner, acc no, balance, history
class Client:
    def __init__(self, names, kra_pin, dob, gender):
        self.names=names
        self.kra_pin=kra_pin
        self.dob=dob
        self.gender=gender
    def print_details(self ):
        print(self.names)
        print(self.kra_pin)
        print(self.dob)
        print(self.gender)


class BankAccount:
    def __init__(self, owner, acc_no, balance):
        self.owner=owner
        self.acc_no=acc_no
        self.balance=balance
    def deposit(self,amount):
        self.balance+= abs(amount)

    def withdraw(self,amount):
        if amount>self.balance:
            print("Not enough money")
        else:
            self.balance -= abs(amount)
    def print_details(self):
        print(self.owner.names)
        print(self.acc_no)
        print(self.balance)
        print("---------------------")


    Jane = Client('jane mwangi', 'A001','1999-01-16','f')
    Ahmed= Client('ahmed','A002','2003-06-07','M')


# dob = '18.01.2026'
#
# today = date.today()
#
# print(f"{today.day}/{today.month}/{today.year}")






