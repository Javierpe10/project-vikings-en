import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self_health = health
        self_strength = strength
    
    def attack(self):
       return self_stength  

    def receiveDamage(self, damage):
        self_health -= damage 
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(self, name, health, strength)
        self.name = name

    def battleCry(self):
        return "Odin Owns You All"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here

    def receiveDamage(self, damage):
        # your code here

# WAAAAAAAAAGH

class War():
    def __init__(self):
        # your code here

    def addViking(self, viking):
        # your code here
    
    def addSaxon(self, saxon):
        # your code here
    
    def vikingAttack(self):
        # your code here
    
    def saxonAttack(self):
        # your code here

    def showStatus(self):
        # your code here
    pass


