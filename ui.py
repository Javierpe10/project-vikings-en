# ui.py
import os
import time

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
