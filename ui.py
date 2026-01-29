# ui.py
# -----
# Handles ALL presentation-related concerns:
# - Sound effects and music (pygame)
# - Timing and pauses
# - Terminal UI (health bars, round framing, cinematic output)

import pygame
import random
import os
import time

# Initialize Pygame and Mixer (required for sound playback)
pygame.init()
pygame.mixer.init()

# --- CONSTANTS & CONFIG ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# A display surface is required by pygame even if we are text-based
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Vikings vs Saxons")

# --- SOUND CONFIG ---
# Maps sound categories to available audio files
SOUND_POOL = {
    "hits": ["sounds/Metal Thud.mp3"], 
    "cries": ["sounds/Battle Cry - High Pitch.mp3", "sounds/Battle Agony Moans.mp3"],
    "ambience": ["sounds/battle.mp3", "sounds/battle.wav"],
    "intro": ["sounds/intro.mp3"],
    "results": ["sounds/results.mp3", "sounds/battle_results.wav"],
    "archers": ["sounds/archers.wav"]
}

# Cache for short sound effects (loaded once)
SFX_CACHE = {}

def load_sounds():
    """
    Preloads short sound effects into memory.
    Long ambience tracks are streamed instead.
    """
    print("Loading sounds...")
    for category in ["hits", "cries", "archers"]:
        SFX_CACHE[category] = []
        for filename in SOUND_POOL.get(category, []):
            if os.path.exists(filename):
                try:
                    sound = pygame.mixer.Sound(filename)
                    sound.set_volume(0.6)
                    SFX_CACHE[category].append(sound)
                    print(f"  [+] Loaded {filename}")
                except Exception as e:
                    print(f"  [!] Failed to load {filename}: {e}")
            else:
                print(f"  [!] Missing file: {filename}")

def play_sfx(category, maxtime=0, fade_ms=0):
    """
    Plays a random sound effect from a given category.
    Used for hits, deaths, and special actions.
    """
    if category in SFX_CACHE and SFX_CACHE[category]:
        random.choice(SFX_CACHE[category]).play(maxtime=maxtime, fade_ms=fade_ms)

def play_music_snippet(category, fade_ms=2000):
    """
    Streams a random background track from disk.
    Used for ambience, intro, and results music.
    """
    files = SOUND_POOL.get(category, [])
    if not files:
        return

    filename = random.choice(files)
    if os.path.exists(filename):
        try:
            pygame.mixer.music.load(filename)
            start_offset = random.uniform(0, 30.0)
            pygame.mixer.music.play(start=start_offset, fade_ms=fade_ms)
            pygame.mixer.music.set_volume(0.4)
        except Exception as e:
            print(f"Music error: {e}")

def stop_music(fade_ms=1000):
    """Fades out any currently playing background music."""
    pygame.mixer.music.fadeout(fade_ms)

# --- BASIC UI HELPERS ---

def clear():
    """Clears the terminal screen (cross-platform)."""
    os.system("cls" if os.name == "nt" else "clear")

def pause(seconds=0.8):
    """Adds a small delay for pacing and readability."""
    time.sleep(seconds)

def health_bar(unit, max_health=300, length=10):
    """
    Builds a colored health bar for a unit.
    Color reflects remaining health percentage.
    """
    current = max(unit.health, 0)
    ratio = current / max_health
    filled = max(0, min(length, int(ratio * length)))

    if ratio > 0.6:
        block = "🟩"
    elif ratio > 0.3:
        block = "🟨"
    else:
        block = "🟥"

    return block * filled + "⬛" * (length - filled)

def display_armies(war):
    """
    Original army display (kept for compatibility).
    """
    print("\n🛡️ VIKINGS")
    for v in war.vikingArmy:
        print(f"  {v.name} [{health_bar(v)}] {v.health} HP")

    print("\n⚔️ SAXONS")
    for s in war.saxonArmy:
        print(f"  Saxon [{health_bar(s, 100)}] {s.health} HP")

# --- CINEMATIC CLI ADDITIONS ---
# These functions improve readability and presentation
# without affecting game mechanics or sound behavior.

def print_round_header(round_number):
    """Prints a cinematic round title."""
    print("\n" + "═" * 36)
    print(f"{'⚔️  ROUND ' + str(round_number):^36}")
    print("═" * 36 + "\n")

def print_action(title, result):
    """
    Prints a formatted action block.
    Uses symbols to distinguish damage from death.
    """
    print(title)
    if result:
        if "died" in str(result).lower() or "dead" in str(result).lower():
            print(f"    └─ 💀 {result}")
        else:
            print(f"    └─ 💥 {result}")

def print_battle_status_cinematic(war):
    """
    Cinematic version of the army status display.
    Groups armies and uses colored health bars.
    """
    print("\n" + "═" * 12 + "  BATTLE STATUS  " + "═" * 12 + "\n")

    print("🛡️ VIKINGS")
    for v in war.vikingArmy:
        print(f"  {v.name:<8} [{health_bar(v)}] {v.health} HP")

    print("\n⚔️ SAXONS")
    for s in war.saxonArmy:
        label = "Monk" if s.__class__.__name__ == "WarriorMonk" else "Saxon"
        max_hp = 90 if label == "Monk" else 100
        print(f"  {label:<8} [{health_bar(s, max_hp)}] {s.health} HP")
