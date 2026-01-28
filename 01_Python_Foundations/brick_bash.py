import turtle 
import random

#Parent class
class Brick:
    def __init__(self,x,y,color,health):
        self.avatar = turtle.Turtle()
        self.avatar.shape("square")
        self.avatar.shapesize(stretch_wid=1, stretch_len=3) # Make it rectangular
        self.avatar.color(color)
        self.avatar.penup()
        self.avatar.goto(x, y)
        self.avatar.speed(0)
        self.health = health
        self.is_active = True

    def take_hit(self):
        #default behavoir - loose health
        self.health -= 1 
        if self.health <= 0:
            self.break_brick()

    def break_brick(self):
        self.is_active = False
        self.avatar.hideturtle()
        # Move it off screen so ball doesn't hit it again
        self.avatar.goto(1000, 1000)

# Children class(inheritance & Overriding)

class GlassBrick(Brick):
    def __init__(self, x, y):
        super().__init__(x, y,"cyan",1)
    #No override needed

class SteelBrick(Brick):
    def __init__(self, x, y, color, health):
        super().__init__(x, y, "grey", 9999)
        #steel is tough , inif health
    def take_hit(self):
        print("clang!")

class TNTBrick(Brick):
    def __init__(self, x, y):
        # TNT is red and volatile
        super().__init__(x, y, "red", 1)

    # OVERRIDE: Explodes when hit
    def break_brick(self):
        print("BOOM! TNT Exploded!")
        self.avatar.shapesize(4, 4) # Visual explosion
        self.avatar.color("orange")
        # In a real game, this would destroy neighbors too
        super().break_brick() # Then vanish

def create_brick(brick_type, x, y):
    try:
        if brick_type == "glass":
            return GlassBrick(x, y)
        elif brick_type == "steel":
            return SteelBrick(x, y)
        elif brick_type == "tnt":
            return TNTBrick(x, y)
        else:
            #  RAISING AN EXCEPTION
            raise ValueError(f"Unknown brick type: {brick_type}")
    except ValueError as e:
        #  CATCHING THE EXCEPTION
        print(f"Error caught: {e}. Spawning a default Glass brick instead.")
        return GlassBrick(x, y) # Fail-safe
    
screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)

# Create the Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, -100)
ball.dx = 3
ball.dy = 3

# Create the Wall of Bricks
bricks = []
start_x = -200
start_y = 200

# We intentionally put a typo ("mud") to test Exception Handling
layout = ["glass", "steel", "glass", "tnt", "mud", "glass", "steel"]

for i, b_type in enumerate(layout):
    # Determine position
    x_pos = start_x + (i * 70)
    
    # Factory Function with Error Handling
    new_brick = create_brick(b_type, x_pos, start_y)
    bricks.append(new_brick)

print("GAME START! Watch the console for 'CLANG' and 'BOOM'")

while True:
    screen.update()
    
    # Move Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Wall Collisions
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.dx *= -1
    if ball.ycor() > 280:
        ball.dy *= -1
    if ball.ycor() < -280: # Floor (Game Over condition normally)
        ball.dy *= -1 

    # Brick Collisions
    for brick in bricks:
        if brick.is_active:
            # Simple collision check
            if ball.distance(brick.avatar) < 40:
                ball.dy *= -1 # Bounce
                brick.take_hit() # Polymorphism! (Glass breaks, Steel clangs)
        