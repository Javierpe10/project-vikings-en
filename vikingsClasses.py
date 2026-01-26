import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
       return self.strength  

    def receiveDamage(self, damage):
        self.health -= damage 

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

    #we need to put comment?

# WAAAAAAAAAGH

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
      
    
    def vikingAttack(self):
        defender = random.choice(self.saxonArmy)
        attacker = random.choice(self.vikingArmy)

        result = defender.receiveDamage(attacker.attack())

        if defender.health <= 0:
            self.saxonArmy.remove(defender)
        return result
    def saxonAttack(self):
        defender = random.choice(self.vikingArmy)
        attacker = random.choice(self.saxonArmy)

        result = defender.receiveDamage(attacker.attack())

        if defender.health <= 0:
            self.vikingArmy.remove(defender)
        return result

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."



