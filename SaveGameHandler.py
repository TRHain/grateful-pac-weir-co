"""
SaveGameHandler: Handles saving/loading game data
"""

import json

def save_game_data(game_data):
    """Save game data to JSON."""
    with open("deadpacman_field_notes.json", "w") as f:
        json.dump(game_data, f)

def load_game_data():
    """Load game data from JSON."""
    try:
        with open("deadpacman_field_notes.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"current_level": 1,
                "dots_eaten": 0,
                "fruits_consumed": [],
                "bear_head_damage": 0}
