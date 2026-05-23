"""
ResponsiveUI: Tkinter + Pygame Hybrid UI
"""

import tkinter as tk
from tkinter import messagebox

class DeadPacManUI:
    """Handles UI for all devices (iOS, Mac, Windows)."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DeadPac-Man™")
        self.root.config(bg="black")

    def show_load_save(self):
        """Show save game UI with Dead theme."""
        tk.Label(self.root,
                text="📝 DeadPac-Man™ Field Notes",
                font=("Helvetica", 24), bg="black", fg="gold").pack()

        tk.Button(self.root,
                text="Load Game",
                command=self.load_game).pack()

        tk.Button(self.root,
                text="New Game",
                command=self.new_game).pack()

        # Dead-themed footer
        tk.Label(self.root,
                text="Last Level:[55]",
                font=("Helvetica", 10), bg="black", fg="navy").pack()

        self.root.mainloop()

    def load_game(self):
        """Load game data from JSON."""
        try:
            with open("deadpacman_field_notes.json", "r") as f:
                data = json.load(f)
                messagebox.showinfo("Game Loaded",
                                 f"Level: {data['current_level']}\n"
                                 f"Bear Head Damage: {data['bear_head_damage']}")
        except FileNotFoundError:
            messagebox.showinfo("New Game", "No saved game! Start fresh.")

    def new_game(self):
        """Reset game and create blank save data."""
        self.root.destroy()
        save_data = {"current_level": 1,
                    "dots_eaten": 0,
                    "fruits_consumed": [],
                    "bear_head_damage": 0}
