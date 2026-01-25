import turtle
import random
class Racer:
     def __init__(self,color,y_position):
       self.avatar = turtle.Turtle()
       self.avatar.shape("turtle")
       self.avatar.color(color)
       self.avatar.speed(0) # Fastest Drawing speed
       self.avatar.penup() #dont draw yet

       #setup position - unique
       self.avatar.goto(-200,y_position)
       self.avatar.pendown()

     def move(self):
      #each object moves a random amount
      distance = random.randint(1,10)
      self.avatar.forward(distance)

     def get_x(self):
      return self.avatar.xcor()


screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Object Race")

#Instantiating or creating the objects
racer_1 = Racer("cyan", 50)
racer_2 = Racer("magenta", 0)
racer_3 = Racer("lime", -50)

#Game loop

is_racing = True
while is_racing:
  racer_1.move()
  racer_2.move()
  racer_3.move()

  #checking winner
  for racer in [racer_1,racer_2,racer_3]:
    if racer.get_x()> 200:
      print(f"The winner is {racer.avatar.pencolor().upper()}!")
      is_racing = False
      break

#To keep window open
screen.exitonclick()