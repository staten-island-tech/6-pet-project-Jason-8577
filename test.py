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

print("1: Rest")
print("2: Eat.")
print("3: play.")
print("4: show_status.")
print("5: Exit")

class pet:
    def __init__(self, name, happiness, hunger, energy):
        self.name = name
        self.__happiness = happiness
        self.hunger = hunger
        self.energy = energy
        
    def rest(self, sleep):
        self.energy += sleep

    def eat(self):
        self.hunger += 10
        self.energy += 5

    def play(self, happy):
        self.__happiness += happy

    def show_status(self):
        print(f"{self.name}'s happiness is {self.__happiness}, and {self.name}'s energy is {self.energy}.")


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")

