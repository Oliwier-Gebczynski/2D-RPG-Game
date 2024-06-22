import json
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

    def to_dict(self):
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "description": self.description
        }

    @staticmethod
    def from_dict(data):
        item_type = data["type"]
        if item_type == "Sword":
            return Sword(data["name"], data["description"], data["attack"])
        elif item_type == "Armor":
            return Armor(data["name"], data["description"], data["defense"])
        elif item_type == "GoldenApple":
            return GoldenApple(data["name"], data["description"], data["healing_power"])
        else:
            raise ValueError(f"Unknown item type: {item_type}")

class Sword(Item):
    def __init__(self, name, description, attack):
        super().__init__(name, description)
        self.attack = attack

    def __str__(self):
        return f"{super().__str__()}\nAttack power: {self.attack}"

    def to_dict(self):
        data = super().to_dict()
        data["attack"] = self.attack
        return data

class Armor(Item):
    def __init__(self, name, description, defense):
        super().__init__(name, description)
        self.defense = defense

    def __str__(self):
        return f"{super().__str__()}\nDefense power: {self.defense}"

    def to_dict(self):
        data = super().to_dict()
        data["defense"] = self.defense
        return data

class GoldenApple(Item):
    def __init__(self, name, description, healing_power):
        super().__init__(name, description)
        self.healing_power = healing_power

    def __str__(self):
        return f"{super().__str__()}\nHealing power: {self.healing_power}"

    def to_dict(self):
        data = super().to_dict()
        data["healing_power"] = self.healing_power
        return data
