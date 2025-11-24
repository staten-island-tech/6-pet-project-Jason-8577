""" class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

Rock = Hero("Rock", 2000, ["sword"])
Rock.buy({"tite": "wood armor", "defense": +5})
print(Rock.__dict__) """

class pet:
    def __init__(self, name, happiness):
        self.name = name
        self.__happiness = happiness

    def play(self, happy):
        self.__happiness += happy
        

    def show_status(self):
        print(f"{self.name}'s happiness is {self.__happiness}")

donkey = pet("donkey", 0)



class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")