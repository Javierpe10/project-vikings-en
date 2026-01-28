# ui.py

import pygame
import random
import os
import time

# Initialize Pygame and Mixer
pygame.init()
pygame.mixer.init()

# --- CONSTANTS & CONFIG ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# We create a display surface because pygame commands often require it, 
# even if we are mostly text-based.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Vikings vs Saxons")

# Sound File Mappings
# Mapping categories to lists of filenames from your 'sounds' directory
SOUND_POOL = {
    "hits": ["sounds/Metal Thud.mp3"], 
    "cries": ["sounds/Battle Cry - High Pitch.mp3", "sounds/Battle Agony Moans.mp3"],
    "ambience": ["sounds/battle.mp3", "sounds/battle.wav"], # Long files
    "intro": ["sounds/intro.mp3"],
    "results": ["sounds/results.mp3", "sounds/battle_results.wav"],
    "archers": ["sounds/archers.wav"]
}

# Cache for loaded Sound objects (only for short SFX)
SFX_CACHE = {}

def load_sounds():
    """
    Preloads short sound effects into memory.
    Long ambience tracks are NOT preloaded to save RAM; specific streaming functions will handle them.
    """
    print("Loading sounds...")
    for category in ["hits", "cries", "archers"]:
        SFX_CACHE[category] = []
        for filename in SOUND_POOL.get(category, []):
            if os.path.exists(filename):
                try:
                    sound = pygame.mixer.Sound(filename)
                    # Lower volume for SFX so they don't deafen
                    sound.set_volume(0.6) 
                    SFX_CACHE[category].append(sound)
                    print(f"  [+] Loaded {filename}")
                except Exception as e:
                    print(f"  [!] Failed to load {filename}: {e}")
            else:
                print(f"  [!] Missing file: {filename}")

def play_sfx(category, maxtime=0, fade_ms=0):
    """
    Plays a random Sound object from the loaded cache for a given category.
    Allows for overlapping sounds (SFX layer).
    """
    if category in SFX_CACHE and SFX_CACHE[category]:
        sound = random.choice(SFX_CACHE[category])
        # play() returns a Channel object
        sound.play(maxtime=maxtime, fade_ms=fade_ms)

def play_music_snippet(category, fade_ms=2000):
    """
    Streams a random long file from disk as background music.
    Supports random start offsets to create variety.
    """
    files = SOUND_POOL.get(category, [])
    if not files:
        return

    filename = random.choice(files)
    if os.path.exists(filename):
        try:
            pygame.mixer.music.load(filename)
            
            # Random start point logic
            # Since we don't know exact duration without probing, we pick a safe random start
            # or start from 0 if it's a short clip. 
            # ideally, 'battle.mp3' is long.
            start_offset = random.uniform(0, 30.0) # Start anywhere in first 30s
            
            print(f"🎵 Playing atmosphere: {filename} (Offset: {start_offset:.1f}s)")
            pygame.mixer.music.play(start=start_offset, fade_ms=fade_ms)
            pygame.mixer.music.set_volume(0.4) # Background level
        except Exception as e:
            print(f"Music error: {e}")

def stop_music(fade_ms=1000):
    pygame.mixer.music.fadeout(fade_ms)

# --- VISUAL UI ---

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause(seconds=0.8):
    time.sleep(seconds)

def health_bar(unit, max_health=300, length=20):
    current = max(unit.health, 0)
    ratio = current / max_health
    filled = int(ratio * length)
    return "█" * filled + "-" * (length - filled)

def display_armies(war):
    print("\n🛡️ VIKINGS")
    for v in war.vikingArmy:
        print(f"  {getattr(v, 'name', 'Unknown')} [{health_bar(v)}] {v.health} HP")

    print("\n⚔️ SAXONS")
    for s in war.saxonArmy:
        print(f"  Saxon [{health_bar(s, max_health=100)}] {s.health} HP")
