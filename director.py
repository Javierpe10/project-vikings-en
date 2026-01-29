# director.py
# -----------
# Orchestrates the flow of the game:
# - Controls rounds
# - Triggers attacks
# - Calls UI and sound helpers

import random
from ui import (
    pause,
    load_sounds,
    play_sfx,
    play_music_snippet,
    stop_music,
    print_round_header,
    print_action,
    print_battle_status_cinematic
)

INTRO_LINES = [
    "⚔️ Steel clashes on the battlefield!",
    "🌫️ A cold wind sweeps across the warzone...",
    "🔥 The war drums echo across the land!",
]

class GameDirector:
    def __init__(self, war):
        """
        Initializes the director with a War instance.
        Loads sound effects once at startup.
        """
        self.war = war
        self.round = 1
        self.log = []
        load_sounds()

    def intro(self):
        """
        Plays intro music and displays a random intro line.
        """
        play_music_snippet("intro", fade_ms=500)
        print("\n" + "=" * 40)
        print(random.choice(INTRO_LINES))
        print("=" * 40 + "\n")
        pause(2)

    def play_round(self):
        """
        Plays a single round of combat:
        - Displays round header
        - Executes Viking attack
        - Executes Saxon counterattack
        - Displays battle status
        """
        print_round_header(self.round)

        # Change ambience at key moments
        if self.round == 1 or self.round % 5 == 0:
            play_music_snippet("ambience", fade_ms=2000)

        # Viking attack phase
        if self.war.vikingArmy and self.war.saxonArmy:
            result = self.war.vikingAttack()
            print_action("🛡️  Vikings charge forward", result)
            self.log.append(result)

            play_sfx("cries" if "died" in str(result).lower() else "hits")
            pause()

        # Saxon counterattack phase
        if self.war.vikingArmy and self.war.saxonArmy:
            result = self.war.saxonAttack()
            print_action("⚔️  The Saxons strike back", result)
            self.log.append(result)

            play_sfx("cries" if "died" in str(result).lower() else "hits")
            pause()

        # Show current battle status
        print_battle_status_cinematic(self.war)
        self.round += 1

    def game_over(self):
        """
        Ends the game:
        - Stops ambience
        - Plays results music
        - Displays final outcome
        - Writes battle log to disk
        """
        stop_music(fade_ms=1000)
        pause(1)
        play_music_snippet("results", fade_ms=1000)

        print("\n🏁 GAME OVER")
        print(self.war.showStatus())

        with open("battle_log.txt", "w") as f:
            for line in self.log:
                f.write(line + "\n")

        print("\n(Press Ctrl+C to exit)")
        pause(5)
