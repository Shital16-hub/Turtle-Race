# Turtle Race

import turtle
import random


screen = turtle.Screen()
screen.setup(height=400, width=500)
user_input = screen.textinput(title="Make your bet.", prompt="Which turtle will win race? Enter colour:  ")
turtle_colour = ["red", "yellow", "green", "blue", "coral", "orange", "cyan"]
turtle_y_posotion = [-100, -60, -20, 20, 60, 100 ]
turtle_lst = []
is_race_on = False


for turtles in range(6):
    new_turtle = turtle.Turtle(shape='turtle')
    new_turtle.color(turtle_colour[turtles])
    new_turtle.penup()
    new_turtle.goto(-230, turtle_y_posotion[turtles])
    turtle_lst.append(new_turtle)

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in turtle_lst:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_input == winning_color:
                print(f"You have won, The color of winning turtle is :{winning_color}")
            else:
                print(f"You have lost, The color of winning turtle is :{winning_color}")

        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)


screen.exitonclick()