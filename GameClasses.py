"""
GameClasses: BearHead and Fruit Logic
"""

from DeadPacManCore import DeadPacManCore

class BearHead(pygame.sprite.Sprite):
    """BearHead class for Pac-Man theme."""
    def __init__(self):
        self.image = DeadPacManCore.draw_fruit("Guitar")  # Default: Bear Head
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.level = 1
        self.score = 0
        self.damage = 0

    def move(self, direction):
        """Move BearHead in 4 directions (up/down/left/right)."""
        self.rect.x += direction[0] * 5
        self.rect.y += direction[1] * 5

    def eat_fruit(self, fruit):
        """Eat fruit and apply Dead-themed bonuses."""
        self.score += DeadPacManCore.FRUIT_TYPES[fruit]["Base Score"]
        self.damage += DeadPacManCore.FRUIT_TYPES[fruit]["Damage Bonus"]

class Fruit(pygame.sprite.Sprite):
    """Fruit class for Dead-themed power-ups."""
    def __init__(self, fruit_type, pos):
        self.fruit_type = fruit_type
        self.image = DeadPacManCore.draw_fruit(self.fruit_type)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
