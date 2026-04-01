"""Ball visible state for the game."""

import pygame
import random
from backdrop import Backdrop
from ball import Ball
from states.base_state import BaseGameState


class BallVisible(BaseGameState):
    """The ball visible state of the game."""
    
    def __init__(self, game):
        """Initialize the ball visible state.
        
        Args:
            game: Reference to the main Game instance
        """
        self.game = game
        self.backdrop = Backdrop(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        
        # Create ball at random position
        random_position = random.choice(["left", "middle", "right"])
        self.ball = Ball(random_position)
    
    def on_key_down(self, key: int):
        """Handle key press events.
        
        Args:
            key: The pygame key code
        """
        if key == pygame.K_SPACE:
            # Return to start screen
            from game import GameState
            self.game.change_state(GameState.START_SCREEN)
    
    def update(self, dt: float):
        """Update the ball visible state.
        
        Args:
            dt: Delta time in seconds
        """
        # Update backdrop (moving down)
        self.backdrop.update(dt, direction="down")
    
    def draw(self, surface: pygame.Surface):
        """Draw the ball visible state.
        
        Args:
            surface: The pygame surface to draw on
        """
        # Draw backdrop
        self.backdrop.draw(surface)
        
        # Draw border
        self._draw_border(surface)
        
        # Draw ball
        self.ball.draw(surface)
        
        # Draw message bar
        self._draw_message_bar(surface, "Press SPACE to continue")
