import time
import random
import sys
import select
import tty
import termios

class DinoGame:
    def __init__(self):
        self.width = 40
        self.dino_y = 0      # Height (0 = Ground)
        self.velocity = 0    # Speed of jump
        self.cactus_pos = 35 # Enemy start position
        self.score = 0
        self.is_running = True

    def is_key_pressed(self):
        # The Mac "Hack" to check for input without stopping the code
        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

    def update(self):
        # 1. Physics (Gravity)
        if self.dino_y > 0 or self.velocity > 0:
            self.dino_y += self.velocity
            self.velocity -= 0.3 # Gravity pulls down
        
        # Floor collision
        if self.dino_y <= 0:
            self.dino_y = 0
            self.velocity = 0

        # 2. Input (Jump)
        if self.is_key_pressed():
            # Consume the key so it doesn't build up
            sys.stdin.read(1)
            if self.dino_y == 0: # Can only jump if on ground
                self.velocity = 2.5 # Launch force

        # 3. Enemy Movement
        self.cactus_pos -= 1
        if self.cactus_pos < 0:
            self.cactus_pos = 39 # Respawn on right
            self.score += 1

        # 4. Collision Detect
        # If cactus is at same column as Dino (approx column 5)
        if 4 <= self.cactus_pos <= 6 and self.dino_y < 1:
            self.is_running = False

    def draw(self):
        # Create empty sky
        # Round y to nearest integer for drawing
        dino_height = int(self.dino_y)
        
        # Build the scene string
        # We need 10 lines of "sky"
        scene = "\033[H\033[J" # Clear screen command
        scene += f"SCORE: {self.score}\n"
        
        for y in range(8, -1, -1):
            line = ""
            for x in range(self.width):
                char = " "
                
                # Draw Dino at x=5
                if x == 5 and y == dino_height:
                    char = "🦖"
                
                # Draw Cactus
                elif x == self.cactus_pos and y == 0:
                    char = "🌵"
                
                line += char
            scene += line + "\n"
            
        scene += "=" * self.width # The ground
        print(scene)

    def start(self):
        # SAVE TERMINAL SETTINGS
        old_settings = termios.tcgetattr(sys.stdin)
        try:
            # Set terminal to 'raw' mode (reads keys instantly)
            tty.setcbreak(sys.stdin.fileno())
            
            print("Game Starting... Press SPACE to Jump!")
            time.sleep(1)
            
            while self.is_running:
                self.update()
                self.draw()
                time.sleep(0.08) # Game Speed
                
            print(f"\n💥 GAME OVER! Score: {self.score}")
            
        finally:
            # RESTORE TERMINAL SETTINGS (Crucial!)
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

if __name__ == "__main__":
    game = DinoGame()
    game.start()