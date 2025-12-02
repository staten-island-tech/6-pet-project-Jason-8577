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

    def eat(self):
        self.hunger += 5
        self.energy += 2
        self.__happiness += 2
        print(f"{self.name} is eating {user_input}.")
        print(f"{self.name}'s happiness, energy, and hunger is now:")
        print(f"Happiness: {self.__happiness}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        
    def play(self):
        self.energy -= 2
        self.__happiness += 2
        print(f"{self.name} is playing {user_input}, Happiness level is {self.__happiness} and Energy level is {self.energy}.")

    def show_status(self):
        print(f"{self.name}'s status:")
        print(f"Happiness level: {self.__happiness}.")
        print(f"Energy level: {self.energy}.")
        print(f"Hunger level: {self.hunger}.")
        
donkey = pet("donkey", 10, 10, 10)

while True:

    print("1: eat.")
    print("2: play.")
    print("3: Show_Status.")
    print("4: quit/stop the game.")

    inputs = int(input("input a number."))

    if inputs == 1:
        user_input = input("What would you like to feed donkey?")
        donkey.eat()

    elif inputs == 2:
        user_input = input("What would you like to play with donkey?")
        donkey.play()

    elif inputs == 3:
        donkey.show_status()
    
    elif inputs == 4:
        print("Final happiness, energy, and hunger level:")
        donkey.show_status()
        break