from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Racing Game",
                              prompt="Who would you like to bet on? aqua,blue,red,purple,maroon,green")

y_pos = [-150, -90, -30, 30, 90, 150]
colour_list = ["aqua", "blue", "red", "purple", "maroon", "green"]
turtles_list = []

for index in range(6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colour_list[index])
    new_turtle.penup()
    new_turtle.goto(-230, y_pos[index])
    turtles_list.append(new_turtle)

if user_input:
    is_race_on = True

while is_race_on:
    for turtles in turtles_list:
        if turtles.xcor() > 225:
            is_race_on = False
            tur_col = turtles.pencolor()
            if user_input == tur_col:
                print(f"You won. {tur_col} turtle won the race.")
            else:
                print(f"You lost. {tur_col} turtle won the race.")
            break
        rand_distance = random.randint(1, 10)
        turtles.forward(rand_distance)

screen.exitonclick()
