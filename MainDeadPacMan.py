"""
MainDeadPacMan.py: Entry Point for GitHub Upload
"""

from DeadPacManCore import DeadPacManCore
from GameClasses import BearHead, Fruit
from DeadLevelGenerator import generate_dead_levels
from SaveGameHandler import save_game_data, load_game_data
from ResponsiveUI import DeadPacManUI

# --- GitHub Upload Ready ---
def main():
    """Run DeadPac-Man™."""
    # Generate levels
    levels = generate_dead_levels()

    # Create BearHead
    bear_head = BearHead()

    # Create UI
    ui = DeadPacManUI()
    ui.show_load_save()

    # Save initial data
    game_data = {"current_level": 1,
                "dots_eaten": 0,
                "fruits_consumed": [],
                "bear_head_damage": 0}
    save_game_data(game_data)

    # Start game loop
    print("🎵 'Why Should I Be Blue?' – DeadPac-Man™ Game Started!")
    print("📝 Save file: deadpacman_field_notes.json")

if __name__ == "__main__":
    main()
