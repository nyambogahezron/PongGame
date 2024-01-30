import turtle

window = turtle.Screen()
window.title('PONG GAME')
window.bgcolor('orange')
window.setup(width=800, height=600)
window.tracer(0)


# Paddle A  
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B  
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.color('white')
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball 
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)

# Move Paddle A
# Up

def paddle_a_up():
    y = paddle_a.ycor()
    y +=20
    paddle_a.sety(y)

# Keyboard moving key listen
window.listen()
window.onkeypress(paddle_a_up, 'a')

# Down 
def paddle_a_down():
    y = paddle_a.ycor()
    y -=20
    paddle_a.sety(y)

# Keyboard moving key listen
window.listen()
window.onkeypress(paddle_a_down, 'z')


# Move Paddle B
# Up

def paddle_b_up():
    y = paddle_b.ycor()
    y +=20
    paddle_b.sety(y)

# Keyboard moving key listen
window.listen()
window.onkeypress(paddle_b_up, 'l')

# Down 
def paddle_b_down():
    y = paddle_b.ycor()
    y -=20
    paddle_b.sety(y)

# Keyboard moving key listen
window.listen()
window.onkeypress(paddle_b_down, 'm')

# Main Game loop 
while True:
    window.update()