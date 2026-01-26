# director.py
import random
from ui import pause, display_armies

INTRO_LINES = [
    "⚔️ Steel clashes on the battlefield!",
    "🌫️ A cold wind sweeps across the warzone...",
    "🔥 The war drums echo across the land!",
]

class GameDirector:
    def __init__(self, war):
        self.war = war
        self.round = 1
        self.log = []

    def intro(self):
        print(random.choice(INTRO_LINES))
        pause()

    def play_round(self):
        print(f"\n===== ⚔️ ROUND {self.round} =====")
        self.intro()

        if self.war.vikingArmy and self.war.saxonArmy:
            result = self.war.vikingAttack()
            print("🛡️ Viking attack:", result)
            self.log.append(result)
            pause()

        if self.war.vikingArmy and self.war.saxonArmy:
            result = self.war.saxonAttack()
            print("⚔️ Saxon attack:", result)
            self.log.append(result)
            pause()

        display_armies(self.war)
        self.round += 1

    def game_over(self):
        print("\n🏁 GAME OVER")
        print(self.war.showStatus())

        with open("battle_log.txt", "w") as f:
            for line in self.log:
                f.write(line + "\n")
