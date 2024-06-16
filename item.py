class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

class Sword(Item):
    def __init__(self, name, description, attack):
        super().__init__(name, description)
        self.attack = attack

    def __str__(self):
        return f"{super().__str__()}\nAttack power: {self.attack}"

class Armor(Item):
    def __init__(self, name, description, defense):
        super().__init__(name, description)
        self.defense = defense

    def __str__(self):
        return f"{super().__str__()}\nDefense power: {self.defense}"

class GoldenApple(Item):
    def __init__(self, name, description, healing_power):
        super().__init__(name, description)
        self.healing_power = healing_power

    def __str__(self):
        return f"{super().__str__()}\nHealing power: {self.healing_power}"