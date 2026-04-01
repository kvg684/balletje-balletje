"""Backdrop system for geometric patterns."""

import pygame
import math
import random


class Backdrop:
    """Manages the moving geometric backdrop."""
    
    def __init__(self, width: int, height: int):
        """Initialize the backdrop with dimensions."""
        self.width = width
        self.height = height
        self.offset_x = 0.0  # Horizontal offset
        self.offset_y = 0.0  # Vertical offset
        self.speed = 80  # pixels per second
        self.pattern_size = 40  # Size of repeating pattern
    
    def update(self, dt: float, direction: str = "down"):
        """Update backdrop position.
        
        Args:
            dt: Delta time in seconds
            direction: "up", "down", "left", "right", or corners like "top_left", "top_right", 
                     "bottom_left", "bottom_right", or "random" for random corner movement
        """
        # Handle random by picking a random corner
        if direction == "random":
            direction = random.choice(["top_left", "top_right", "bottom_left", "bottom_right"])
        
        dx = 0.0
        dy = 0.0
        
        if direction == "up":
            dy = -self.speed * dt
        elif direction == "down":
            dy = self.speed * dt
        elif direction == "left":
            dx = -self.speed * dt
        elif direction == "right":
            dx = self.speed * dt
        elif direction == "top_left":
            dx = -self.speed * dt
            dy = -self.speed * dt
        elif direction == "top_right":
            dx = self.speed * dt
            dy = -self.speed * dt
        elif direction == "bottom_left":
            dx = -self.speed * dt
            dy = self.speed * dt
        elif direction == "bottom_right":
            dx = self.speed * dt
            dy = self.speed * dt
        
        self.offset_x += dx
        self.offset_y += dy
    
    def draw(self, surface: pygame.Surface):
        """Draw the geometric backdrop to the surface."""
        # Calculate fractional offsets within the pattern for seamless tiling
        fractional_offset_x = self.offset_x % self.pattern_size
        fractional_offset_y = self.offset_y % self.pattern_size
        
        # Draw tiles with offsets applied to create scrolling effect
        for y in range(-self.pattern_size, self.height + self.pattern_size, self.pattern_size):
            for x in range(-self.pattern_size, self.width + self.pattern_size, self.pattern_size):
                # Calculate the logical tile positions (for pattern determination)
                logical_x = x - self.offset_x
                logical_y = y - self.offset_y
                self._draw_pattern_tile(surface, x - fractional_offset_x, y - fractional_offset_y, logical_x, logical_y)
    
    def _draw_pattern_tile(self, surface: pygame.Surface, x: float, y: float, logical_x: float, logical_y: float):
        """Draw a single pattern tile.
        
        Args:
            surface: The pygame surface to draw on
            x: X coordinate for visual positioning
            y: Y coordinate for visual positioning
            logical_x: X coordinate for pattern calculation
            logical_y: Y coordinate for pattern calculation
        """
        size = self.pattern_size
        
        # Use alternating colors - black and blue boxes
        color1 = (20, 20, 40)  # Dark blue
        color2 = (0, 0, 0)  # Black
        
        # Create a checkerboard pattern based on tile grid position
        # This ensures the pattern scrolls smoothly without flipping
        tile_x = int(logical_x // size) % 2
        tile_y = int(logical_y // size) % 2
        is_light = (tile_x + tile_y) % 2 == 0
        
        color = color2 if is_light else color1
        
        # Draw the tile at the visual position
        rect = pygame.Rect(x, y, size, size)
        pygame.draw.rect(surface, color, rect)
        
        # Draw diagonal lines
        line_color = (60, 60, 120) if is_light else (30, 30, 60)
        pygame.draw.line(surface, line_color, (x, y), (x + size, y + size), 2)
        pygame.draw.line(surface, line_color, (x + size, y), (x, y + size), 2)
