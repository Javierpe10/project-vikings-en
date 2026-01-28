# director.py
import random
from ui import pause, display_armies, load_sounds, play_sfx, play_music_snippet, stop_music

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
        # Initial Sound Load
        load_sounds()

    def intro(self):
        # Play Intro Music
        play_music_snippet("intro", fade_ms=500)
        
        print("\n" + "="*40)
        print(random.choice(INTRO_LINES))
        print("="*40 + "\n")
        pause(2)

    def play_round(self):
        print(f"\n===== ⚔️ ROUND {self.round} =====")
        
        # Dynamic Soundtrack: Change ambience every few rounds or randomly?
        # For now, let's trigger battle atmosphere at the start of rounds
        if self.round == 1:
            play_music_snippet("ambience", fade_ms=2000)
        elif self.round % 5 == 0:
             # Switch up the track occasionally
             play_music_snippet("ambience", fade_ms=2000)

        if self.war.vikingArmy and self.war.saxonArmy:
            result = self.war.vikingAttack()
            print("🛡️ Viking attack:", result)
            self.log.append(result)
            
            # Sound Trigger Based on Result?
            # If "dead" in result (assuming result string has info), play death cry
            # Otherwise play generic hit
            # Since 'result' might just be a string return, we guess logic:
            if "died" in str(result).lower() or "dead" in str(result).lower():
                play_sfx("cries")
            else:
                play_sfx("hits")
            
            pause()

        if self.war.vikingArmy and self.war.saxonArmy:
            result = self.war.saxonAttack()
            print("⚔️ Saxon attack:", result)
            self.log.append(result)
            
            if "died" in str(result).lower() or "dead" in str(result).lower():
                play_sfx("cries")
            else:
                 # 50% chance to play clash or hit
                 play_sfx("hits")
                 
            pause()

        display_armies(self.war)
        self.round += 1

    def game_over(self):
        stop_music(fade_ms=1000)
        pause(1)
        play_music_snippet("results", fade_ms=1000)
        
        print("\n🏁 GAME OVER")
        print(self.war.showStatus())

        with open("battle_log.txt", "w") as f:
            for line in self.log:
                f.write(line + "\n")
        
        # Keep window open to hear the end music
        print("\n(Press Ctrl+C to exit)")
        pause(5)
