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
    def __init__(self, name, happiness, hunger, energy):
        self.name = name
        self.__happiness = happiness
        self.hunger = hunger
        self.energy = energy
        
    def rest(self):
        self.energy += 50
        self.hunger -= 20

    def eat(self):
        if self.__happiness >= 4:
            return "Donkey is too sad to eat."
        self.hunger += 50
        self.energy += 15
        
    def play(self):
        if self.energy >= 24:
            return "Donkey has insufficient energy."
        if self.hunger >= 14:
            return "Donkey is hungry."
        self.__happiness += 25
        self.energy -= 25
        self.hunger -= 15

    def show_status(self):
        return f"{self.name}'s happiness is {self.__happiness}"
        
donkey = pet("donkey", 100, 100, 100)
print("1: Rest.")
print("2: eat.")
print("3: play.")
print("4: Show_Status.")

user_input = input("Choose an option")










