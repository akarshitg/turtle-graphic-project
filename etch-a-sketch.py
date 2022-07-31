from turtle import Turtle, Screen
anshu = Turtle()
my_screen = Screen()


def move_forwards():
    anshu.forward(10)


def move_backwards():
    anshu.backward(10)


def move_counter_clockwise():
    anshu.left(10)


def move_clockwise():
    anshu.right(10)


def clear_screen():
    anshu.reset()


my_screen. listen()
my_screen.onkey(key='w', fun=move_forwards)
my_screen.onkey(key='s', fun=move_backwards)
my_screen.onkey(key='a', fun=move_counter_clockwise)
my_screen.onkey(key='d', fun=move_clockwise)
my_screen.onkey(key='c', fun=clear_screen)

my_screen.exitonclick()
