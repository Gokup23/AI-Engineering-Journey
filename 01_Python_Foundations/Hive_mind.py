import turtle
import random

class Drone:
    # --- 1. CLASS VARIABLES  ---
    move_speed = 2
    swarm_color = "cyan"
    
    def __init__(self):
        # Unique Instance Setup
        self.t = turtle.Turtle()
        self.t.shape("arrow")
        self.t.penup()
        self.t.speed(0)
        # Random starting spot
        self.t.goto(random.randint(-200, 200), random.randint(-200, 200))
        self.t.setheading(random.randint(0, 360))
        
    def move(self):
        # 2. USING CLASS VARIABLES
        # All drones obey the shared speed and color
        self.t.color(Drone.swarm_color) 
        self.t.forward(Drone.move_speed)
        
        # Bounce off walls
        if abs(self.t.xcor()) > 280 or abs(self.t.ycor()) > 280:
            self.t.right(180)

    # --- 3. CLASS METHOD (The Global Switch) ---
    @classmethod
    def set_mood(cls, mode):
        if mode == "ANGRY":
            cls.move_speed = 10
            cls.swarm_color = "red"
            print(" SWARM MODE: ANGRY")
        elif mode == "CALM":
            cls.move_speed = 2
            cls.swarm_color = "cyan"
            print(" SWARM MODE: CALM")
        elif mode == "PANIC":
            cls.move_speed = 20
            cls.swarm_color = "yellow"
            print(" SWARM MODE: PANIC")
# --- SETUP ---
screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0) # Smooth animation

# Create 20 distinct objects
swarm = []
for _ in range(20):
    swarm.append(Drone())

# --- CONTROLS ---
# We call the CLASS METHOD, not an instance method
screen.listen()
screen.onkey(lambda: Drone.set_mood("ANGRY"), "a") # Press 'a'
screen.onkey(lambda: Drone.set_mood("CALM"), "c")  # Press 'c'
screen.onkey(lambda: Drone.set_mood("PANIC"), "p") # Press 'p'

print("Use Keys: 'A' (Angry), 'C' (Calm), 'P' (Panic)")

# --- LOOP ---
while True:
    screen.update()
    for drone in swarm:
        drone.move()