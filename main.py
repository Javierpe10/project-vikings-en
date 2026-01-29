# main.py
# -------
# Entry point of the Vikings vs Saxons game.
#
# Responsibilities:
# - Set up the initial armies
# - Create the War and GameDirector
# - Run the main game loop
# - End the game cleanly

import random
from vikingsClasses import Viking, Saxon, War
from director import GameDirector
from ui import clear

# Pool of possible Viking names
NAMES = [
    "Harald", "Ivar", "Bjorn", "Ragnar", "Leif",
    "Erik", "Ulf", "Sigurd", "Halfdan", "Sven"
]

def setup_war():
    """
    Creates and initializes a War instance.
    - Adds a random set of Vikings with random stats
    - Adds a fixed number of Saxons
    """
    war = War()

    # Create Viking army
    for name in random.sample(NAMES, 5):
        war.addViking(
            Viking(
                name,
                health=random.randint(150, 200),
                strength=random.randint(70, 110),
            )
        )

    # Create Saxon army
    for _ in range(5):
        war.addSaxon(
            Saxon(
                health=100,
                strength=random.randint(40, 70),
            )
        )

    return war

def main():
    """
    Main game loop.
    - Clears the screen
    - Displays title
    - Runs rounds until the war is over
    """
    clear()
    print("🛡️ VIKINGS VS SAXONS 🗡️\n")

    # Initialize war and director
    war = setup_war()
    director = GameDirector(war)

    # Run the game while both armies are alive
    while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        input("\nPress ENTER to continue...")
        clear()
        director.play_round()

    # End-of-game sequence
    director.game_over()

# Entry-point guard
# Ensures main() only runs when this file is executed directly
if __name__ == "__main__":
    main()

