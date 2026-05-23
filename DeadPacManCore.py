"""
DeadPacMan™ Core: Game Logic & Classes
"""

import pygame
import random
from PIL import Image, ImageDraw

class DeadPacManCore:
    """Manages Dead-themed game rules, colors, and fruit types."""

    # Dead theme colors
    DEAD_COLORS = ["gold", "dark_orange", "navy", "green", "red", "black"]

    # Fruit types with Dead-themed names
    FRUIT_TYPES = {
        "Guitar": "Why Should I Be Blue?",
        "Skeleton": "Lightning Carry Me Away",
        "Mushroom": "The Other Side",
        "PotLeaf": "Truckin’",
        "PHIBubble": "Bubblin’ Over",
        "BillyOak": "Farmers Reel",
        "BobPeggy": "Peggy Sue (Bob Weir Mode)"
    }

    # Draw functions for fruits
    @staticmethod
    def draw_fruit(fruit_type, size=25):
        """Draw fruit using PIL."""
        img = Image.new("RGB", (size, size), "white")
        draw = ImageDraw.Draw(img)
        if fruit_type == "Guitar":
            draw.polygon[(0,0), (22,12), (12,22)], fill=random.choice(DeadPacManCore.DEAD_COLORS))
            draw.polygon[(5,15), (20,15), (15,20)], fill="black")
        elif fruit_type == "Skeleton":
            draw.text((10,10), "💀", fill="black")
        #...[Add other fruit types here]
        return img
