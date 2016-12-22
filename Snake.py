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

snake = turtle.Turtle()
snake.up()
snake.shape("square")
snake.color("red")
snake.ht()

snake_coor = [(0, 0)]

stamps = []

dir_x = 0
dir_y = 0

stop = False

def right(): setDir(1, 0)
def left(): setDir(-1, 0)
def up(): setDir(0, 1)
def down(): setDir(0, -1)

