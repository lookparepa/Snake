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

def set_display():
    tracer = SCREEN.tracer()
    SCREEN.tracer(0)
    
    food.clearstamps(1)
    snake.clearstamps(len(snake_coor))
    
    food.goto(food_coor[0], food_coor[1])
    food.stamp()

    for x, y in snake_coor:
        snake.goto(x, y)
        snake.stamp()
    
    SCREEN.tracer(tracer)

def set_pos():
    global snake_coor, food_coor, stop
    avance()
    if isSelfCollision() or isBorderCollision():
        stop = True
    if isFoodCollision():
        append()
        food_coor = getRandomPosition() 

def isSelfCollision():
    global snake_coor
    return len(set(snake_coor))<len(snake_coor)

def isFoodCollision():
    sx, sy = snake_coor[0]
    fx, fy = food_coor
    distance = ((sx-fx)**2 + (sy-fy)**2)**.5
    return distance<20

def isBorderCollision():
    x, y = snake_coor[0]
    return not (-SIZE//2-50<x<SIZE//2+50) or not (-SIZE//2-50<y<SIZE//2+50)

def avance():
    global snake_coor
    x, y = snake_coor[0]
    x += dir_x*20
    y += dir_y*20
    snake_coor.insert(0, (x, y))
    snake_coor.pop(-1)

def append():
    global snake_coor
    a = snake_coor[-1][:]
    snake_coor.append(a)

def setDir(x, y):
    global dir_x, dir_y
    dir_x = x
    dir_y = y


def right(): setDir(1, 0)
def left(): setDir(-1, 0)
def up(): setDir(0, 1)
def down(): setDir(0, -1)

def gameOver():
    d = turtle.Turtle()
    d.up()
    d.ht()
    d.color("blue")
    d.write("GAME OVER\nScore : %04d" % (len(snake_coor)), align="center", font=("Arial", 30, "bold"))
    SCREEN.onclick(lambda*a:[SCREEN.bye(),exit()])

SCREEN.onkeypress(up, "Up")
SCREEN.onkeypress(down, "Down")
SCREEN.onkeypress(right, "Right")
SCREEN.onkeypress(left, "Left")
SCREEN.listen()
loop()
turtle.mainloop()

