
"""
Modified Black Jack environment for Reinforcement‑Learning Assignment 2.

State tuple: (dealer_face_value 1‑13, player_sum)
Action: 0 = stick, 1 = hit
Reward: +1 win, 0 draw, −1 loss

This is a *forward‑view* implementation only; no eligibility traces here.
"""

from __future__ import annotations
import numpy as np
from typing import Tuple

# card values 1‑13
_CARD_VALUES = np.arange(1, 14)

class BlackjackEnv:
    def __init__(self, seed: int | None = None) -> None:
        self.rng = np.random.default_rng(seed)
        self.reset()

    # ---- Public API -------------------------------------------------- #
    def reset(self) -> Tuple[int, int]:
        """Starts a new game and returns the initial state."""
        self.player_sum = 0
        self.dealer_sum = 0
        self.dealer_face = None

        # Player initial card
        c_val, c_col = self._draw_card()
        self.player_sum = self._apply_colour(self.player_sum, c_val, c_col)

        # Dealer initial card (face‑up)
        c_val, c_col = self._draw_card()
        self.dealer_sum = self._apply_colour(self.dealer_sum, c_val, c_col)
        self.dealer_face = c_val

        return (self.dealer_face, self.player_sum)

    def step(self, action: int):
        """Takes action (0 stick, 1 hit) → (next_state | None, reward, done)."""
        if action == 1:             # --- hit ---
            c_val, c_col = self._draw_card()
            self.player_sum = self._apply_colour(self.player_sum, c_val, c_col)

            if self.player_sum > 21 or self.player_sum < 1:   # bust
                return None, -1, True
            return (self.dealer_face, self.player_sum), 0, False

        # --- stick --- → dealer's turn
        while 1 <= self.dealer_sum < 17:
            c_val, c_col = self._draw_card()
            self.dealer_sum = self._apply_colour(self.dealer_sum, c_val, c_col)

        # Resolve outcome
        if self.dealer_sum > 21 or self.dealer_sum < 1:
            reward = +1
        elif self.player_sum > self.dealer_sum:
            reward = +1
        elif self.player_sum < self.dealer_sum:
            reward = -1
        else:
            reward = 0
        return None, reward, True

    # ---- Helpers ----------------------------------------------------- #
    def _draw_card(self):
        value = int(self.rng.choice(_CARD_VALUES))
        colour = "black" if self.rng.random() < 2/3 else "red"
        return value, colour

    @staticmethod
    def _apply_colour(total: int, value: int, colour: str) -> int:
        return total + value if colour == "black" else total - value
