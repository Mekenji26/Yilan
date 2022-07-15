import turtle
import time
hiz = 0.15

pencere = turtle.Screen()
pencere.title('Yılan Oyunu')
pencere.bgcolor('lightblue')
pencere.setup(width=600, height=600)
pencere.tracer(0)

kafa = turtle.Turtle()
kafa.speed(0)
kafa.shape('circle')
kafa.color('black')
kafa.penup()
kafa.goto(0, 0)
kafa.direction = 'stop'

def move():
    if kafa.direction == 'up':
        y = kafa.ycor()
        kafa.sety(y + 20)
    if kafa.direction == 'down':
        y = kafa.ycor()
        kafa.sety(y - 20)        
    if kafa.direction == 'right':
        x = kafa.xcor()
        kafa.setx(x + 20)    
    if kafa.direction == 'left':
        x = kafa.xcor()
        kafa.setx(x - 20)


def goUp():
    if kafa.direction != 'down':
        kafa.direction='up'
    

def goDown():
    if kafa.direction != 'up':
        kafa.direction='down'
    
    
def goRight():
    if kafa.direction != 'left':
        kafa.direction='right'
    
    
def goLeft():
    if kafa.direction != 'right':
        kafa.direction='left'
    

   



while True:
    pencere.update()
    pencere.listen()

    pencere.onkey(goUp, 'Up')
    pencere.onkey(goDown, 'Down')
    pencere.onkey(goRight, 'Right')
   
    pencere.onkey(goLeft, 'Left')
    move()
    time.sleep(hiz)
    x = kafa.xcor()
    y = kafa.ycor()
    if x==300:
        kafa.goto(0, 0)
        kafa.direction = 'stop'

    if x==-300:
        kafa.goto(0, 0)
        kafa.direction = 'stop'

    if y==300:
        kafa.goto(0, 0)
        kafa.direction = 'stop'

    if y==-300:
        kafa.goto(0, 0)
        kafa.direction = 'stop'

    












