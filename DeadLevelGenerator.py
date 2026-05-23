"""
DeadLevelGenerator: Creates PHISH/Billy modes + Bob Weir levels
"""

from DeadPacManCore import DeadPacManCore
from datetime import datetime

def generate_dead_levels():
    """Generate 55 levels with Dead-themed fruit.
    Returns: List of level data.
    """
    levels = []
    current_level = 1
    for _ in range(55):
        # Base level: 3-8 fruits
        fruit_list = random.choices(["Guitar", "Skeleton", "Mushroom", "PotLeaf"],
                                  k=random.randint(3,8))

        # PHISH mode (levels 6-10)
        if current_level >= 6 and current_level <= 10:
            fruit_list.extend(random.choices(["PHIBubble"], k=random.randint(1,2)))

        # BILLY STRINGS mode (levels 11-15)
        if current_level >= 11 and current_level <= 15:
            fruit_list.extend(random.choices(["BillyOak"], k=random.randint(1,2)))

        # BOB WEIR mode (levels 16-25)
        if current_level >= 16 and current_level <= 25:
            fruit_list.extend(random.choices(["BobPeggy"], k=random.randint(1,3)))

        # Trucking Mode (Aug 3, 2025)
        if datetime.date.today() == datetime.date(2025, 8, 3):
            levels.append(fruit_list)
            messagebox.showinfo("Truckin’ Mode",
                              "🎶 'Truckin’' plays! Level unlocked.")

        levels.append(fruit_list)
        current_level += 1
    return levels
