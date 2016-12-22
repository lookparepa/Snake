import turtle
from random import randint

SIZE = 500

SCREEN = turtle.Screen()
SCREEN.title("snake")
SCREEN.setup(SIZE + 50, SIZE + 50)
SCREEN.bgcolor("grey")

food = turtle.Turtle()
food.up()
food.shape("circle")
food.color("yellow")
food.ht()

def getRandomPosition():
    return (randint(-SIZE//2, SIZE//2), randint(-SIZE//2, SIZE//2))

food_coor = getRandomPosition()