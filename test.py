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
    def __init__(self, name, happiness, play):
        self.name = name
        self.happiness = happiness
        self.play = play

    def play_time(self, happiness, play):
        self.happiness.append(play)
        print(self.happiness)
