# main.py
import random
from vikingsClasses import Viking, Saxon, Archer, War
from director import GameDirector
from ui import clear

NAMES = [
    "Harald", "Ivar", "Bjorn", "Ragnar", "Leif",
    "Erik", "Ulf", "Sigurd", "Halfdan", "Sven"
]

def setup_war():
    war = War()

    viking_names = random.sample(NAMES, 5)
    for name in viking_names:
        war.addViking(
            Viking(
                name,
                health=random.randint(150, 200),
                strength=random.randint(70, 110),
            )
        )

    for _ in range(5):
        war.addSaxon(
            Saxon(
                health=100,
                strength=random.randint(40, 70),
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
