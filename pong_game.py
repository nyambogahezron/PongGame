import turtle
import winsound

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
ball.move_x = 0.3
ball.move_y = 0.3

# score 
score_a = 0
score_b = 0   

# Scores Screen 
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write('Player A: {} Player B: {}'.format(score_a, score_b), align="center", font={'Courier', 26, 'bold'} )


# Footer 
footer = turtle.Turtle()
footer.speed(0)
footer.color('blue')
footer.penup()
footer.hideturtle()
footer.goto(-370, -290)
footer.write("Prayer A [a, z] ", align="left", font={'Times', 26, 'bold'} )
 
footer_b = turtle.Turtle()
footer_b.speed(0)
footer_b.color('blue')
footer_b.penup()
footer_b.hideturtle()
footer_b.goto(180, -290)
footer_b.write("Prayer B [Up And Down Arrow Key] ", align="left", font={'Times', 26, 'bold'} )

# Move Paddle A
# Up

def paddle_a_up():
    y = paddle_a.ycor()
    y +=20
    paddle_a.sety(y)


# Down 
def paddle_a_down():
    y = paddle_a.ycor()
    y -=20
    paddle_a.sety(y)

# Move Paddle B
# Up

def paddle_b_up():
    y = paddle_b.ycor()
    y +=20
    paddle_b.sety(y)


# Down 
def paddle_b_down():
    y = paddle_b.ycor()
    y -=20
    paddle_b.sety(y)

# Keyboard moving key listen
window.listen()
window.onkeypress(paddle_a_up, 'a')
window.onkeypress(paddle_a_down, 'z')
window.onkeypress(paddle_b_up, 'Up')
window.onkeypress(paddle_b_down, 'Down')

# Main Game loop 
while True:
    window.update()

    # Move the ball 
    ball.setx(ball.xcor() + ball.move_x)
    ball.sety(ball.ycor() + ball.move_y)

    # y-axis Border Checking 
    if ball.ycor() > 290:
        ball.sety(290)
        ball.move_y *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.move_y *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)


    # y-axis Border Checking 
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.move_x *= -1
        score_a += 1
        pen.clear()
        pen.write('Player A: {} Player B: {}'.format(score_a, score_b), align="center", font={'Courier', 26, 'bold'} )

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.move_x *= -1
        score_b += 1
        pen.clear()
        pen.write('Player A: {} Player B: {}'.format(score_a, score_b), align="center", font={'Courier', 26, 'bold'} )



    # Ball and Paddle collisions
    if (ball.xcor() > 340 and ball.xcor() < 350)and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.move_x *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)


    if (ball.xcor() < -340 and ball.xcor() > -350)and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.move_x *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

