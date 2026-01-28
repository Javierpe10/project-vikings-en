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

#Archer
#Javier: Create test for Archers

class Archer(Soldier):# Javier: Creat Archer with 20% probability of missing
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def battleCry(self):
        return "Loose the arrows!"
    
    def shootArrow(self):
        if random.random() < 0.20:
            return 0
        return self.strength + random.randint(0, 5)#randomness of damage
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"An Archer has received {damage} point of damage"
        else:
            return "An Archer has died in combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def catapultStone(self):#Javier: create Catapults and probability of 20% of missing
        if random.random() < 0.20:
            return 0
        return self.strength + random.randint(5, 10)#randomness of damage
    
    def blow(self): #Assya: "Saxon can receive hits"
        if random.random() < 0.10:
            return self.strength * 2
        return self.strength
       
    def avoidattack (self): #Assya: Saxons can avoid attack
        if random.random () < 0.20:
            return True
        return False 

    def receiveDamage(self, damage):
        self.health -= damage
        
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

    #we need to put comment? Javier: YES!! With your names if its posible

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

        # Check if Saxon defender avoids the attack
        if hasattr(defender, 'avoidattack') and defender.avoidattack():
            return "Saxon missed the attack!" # Or "Saxon avoided attack"
        
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
    

    
    def ArcherAttack(self):#Javier: Archer attack
        archers = [viking for viking in self.vikingArmy if isinstance(viking, Archer)]#Javier: insistance is for the code now that its an archer in the vikings
        if not archers or not self.saxonArmy:
            return "All dead."
        attacker = random.choice(archers)
        defender = random.choice(self.saxonArmy)

        damage = attacker.shootArrow()
        if damage == 0:
            return "The Archer missed the shot!"

        result = defender.receiveDamage(attacker.shootArrow())

        if defender.health <= 0:
            self.saxonArmy.remove(defender)
        return result

    def CatapultRock(self):#Javier: Catapult attack
        if not self.saxonArmy:
            return "No saxon left."
        
        archers = [viking for viking in self.vikingArmy if isinstance(viking, Archer)]
        if not archers:
            return "No archers left to attack."

        attacker = random.choice(self.saxonArmy)
        defender = random.choice(archers)

        damage = attacker.catapultStone()
        if damage == 0:
            return "The Stone didnt hit anyone!"

        result = defender.receiveDamage(attacker.catapultStone())

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



