import turtle
import random

class Creature:
    def __init__(self, color, shape, speed):
        # Create the visual sprite using the Turtle library
        self.avatar = turtle.Turtle()
        self.avatar.shape(shape)   # 'arrow', 'circle', etc.
        self.avatar.color(color)   # Visual color
        
        # 'penup()' is CRITICAL. 
        # Without this, animals would draw lines everywhere they walk.
        # We want them to move like characters, not draw like pens.
        self.avatar.penup()
        
        # 'speed(0)' means "Instant Drawing", not "Stopped".
        # It tells the computer to update the position immediately without animation lag.
        self.avatar.speed(0)
        
        # Spawn at a random location on the map (-200 to 200)
        self.avatar.goto(random.randint(-200, 200), random.randint(-200, 200))
        
        # Store the movement speed (Wolves will be faster than Rabbits)
        self.speed = speed

    def move_forward(self):
        # Move forward in whatever direction we are currently facing
        self.avatar.forward(self.speed)
        
        # --- PHYSICS ENGINE: WALL BOUNCING ---
        # We check the x and y coordinates. 
        # If they go too far (> 280), we turn them around.
        x, y = self.avatar.pos()
        if x > 280 or x < -280 or y > 280 or y < -280:
            self.avatar.right(180) # Flip direction
            self.avatar.forward(20) # Nudge them back inside the map

    def set_target(self, target_obj):
        # --- VECTOR MATH HELPER ---
        # 'towards()' calculates the angle between me and the target.
        # 'setheading()' rotates my body to face that angle.
        # This replaces lines of complex Trigonometry math!
        angle = self.avatar.towards(target_obj.avatar)
        self.avatar.setheading(angle)

class Wolf(Creature):
    def __init__(self):
        # --- SUPER() ---
        # We call the Parent's __init__ to build the body.
        # We specify: Red color, Arrow shape, Speed 3 (Fast)
        super().__init__("red", "arrow", 3)

    # --- UNIQUE BEHAVIOR ---
    def hunt(self, rabbits):
        # Logic: Find the closest rabbit and run towards it
        closest_rabbit = None
        min_dist = 1000 # Start with a huge number
        
        for r in rabbits:
            # 'distance()' is Pythogoras Theorem (a^2 + b^2 = c^2) built-in
            dist = self.avatar.distance(r.avatar)
            if dist < min_dist:
                min_dist = dist
                closest_rabbit = r
        
        if closest_rabbit:
            self.set_target(closest_rabbit) # Face the rabbit
            self.move_forward()             # Run!

class Rabbit(Creature):
    def __init__(self):
        #rabbits are white, circle-shaped, and slower
        super().__init__("white","circle",2)

        # --- METHOD OVERRIDING ---
    # Rabbits don't hunt; they flee. 
    # This logic is totally different from the Wolf.
    def run_away(self, wolves):
        if len(wolves) > 0:
            closest_wolf = wolves[0]
            
            # Step 1: Look at the wolf
            self.set_target(closest_wolf)
            
            # Step 2: Turn 180 degrees (Look AWAY from the wolf)
            self.avatar.left(180)
            
            # Step 3: Run for your life
            self.move_forward()

#GAME ENGINE SETUP
# ==========================================
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Ecosystem Simulator")

# --- TRACER(0) HACK ---
# This turns OFF automatic animation.
# Instead of drawing 1 frame per move (which is slow and choppy),
# we will manually update the screen once per loop.
# This gives us smooth 60 FPS animation.
screen.tracer(0)

# Create the population lists
pack = []
for _ in range(3):
    pack.append(Wolf()) # Spawn 3 Wolves

colony = []
for _ in range(10):
    colony.append(Rabbit()) # Spawn 10 Rabbits

print("SIMULATION STARTED: Close window to exit.")

# ==========================================
# 5. THE GAME LOOP
# ==========================================
is_running = True
while is_running:
    # 1. Update the Screen (Draw the frame)
    screen.update()
    
    # 2. Move the Wolves
    for wolf in pack:
        wolf.hunt(colony)
    
    # 3. Move the Rabbits
    for rabbit in colony:
        rabbit.run_away(pack)
        
    # 4. Check for Collisions (Eating)
    # We iterate over a COPY of the list (colony[:]) so we can delete items safely
    for rabbit in colony[:]:
        caught = False
        for wolf in pack:
            # If distance is less than 20 pixels, it's a hit
            if wolf.avatar.distance(rabbit.avatar) < 20:
                print("Crunch! 🍖 A rabbit was eaten.")
                rabbit.avatar.hideturtle() # Hide the visual sprite
                colony.remove(rabbit)      # Remove from logic list
                
                # Visual Feedback: Wolf gets fatter
                wolf.avatar.shapesize(1.5, 1.5)
                caught = True
                break # Stop checking other wolves for this rabbit