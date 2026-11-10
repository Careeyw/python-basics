from OOP import Client


class client:
    def __init__(self,names,kra_pin,dob,gender):
        self.names = names
        self.age = kra_pin
        self.dob = dob
        self.gender = gender
    def printdetails(self):
        print(self.names,self.age,self.dob,self.gender)

class bankaccount:
    def __init__(self, owner, acc_no, balance):
        self.owner = owner
        self.acc_no = acc_no
        self.balance = balance
    def deposit(self,amount):
        self.balance += abs(amount)
    def withdraw(self,amount):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance -= abs(amount)
    def print_details(self):
        print(self.owner)
        print(self.acc_no)
        print(self.balance)
        print("---------------------")

jane = Client('jane mwangi', 'A001', '1999-01-16', 'f')
ahmed = Client('ahmed','A002', '1999-01-16', 'M')

acc1 = bankaccount(jane, 1111, 70000)
acc2 = bankaccount(jane, 2222, 20000)
acc3 = bankaccount(ahmed, 33333, 100_000)