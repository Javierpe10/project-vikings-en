# main.py
import random
from vikingsClasses import Viking, Saxon, War
from director import GameDirector
from ui import clear

NAMES = [
    "Harald", "Ivar", "Bjorn", "Ragnar", "Leif",
    "Erik", "Ulf", "Sigurd", "Halfdan", "Sven"
]

def setup_war():
    war = War()

    for _ in range(5):
        war.addViking(
            Viking(
                random.choice(NAMES),
                health=300,
                strength=random.randint(80, 150),
            )
        )

    for _ in range(5):
        war.addSaxon(
            Saxon(
                health=100,
                strength=random.randint(30, 60),
            )
        )

    return war

def main():
    clear()
    print("🛡️ VIKINGS VS SAXONS 🗡️\n")

    war = setup_war()
    director = GameDirector(war)

    while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        input("\nPress ENTER to continue...")
        clear()
        director.play_round()

    director.game_over()

if __name__ == "__main__":
    main()
