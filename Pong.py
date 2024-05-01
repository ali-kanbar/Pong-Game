from turtle import Turtle,Screen
from random import randint
import time
game_on = True
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 1, 5
BALL_SPEED = 8
PADDLE_MOVE_DISTANCE = 20
positions = [(-(SCREEN_WIDTH//2 - 20),0),(SCREEN_WIDTH//2 - 30,0)]
FONT = ("Courier", 40, "normal")

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__(shape="square")
        self.speed("fastest")
        self.penup()
        self.goto(position)
        self.color("white")
        self.shapesize(stretch_len = PADDLE_HEIGHT, stretch_wid = PADDLE_WIDTH)
        self.setheading(90)
        self.create_line()

    def Up(self):
        if self.ycor()<(SCREEN_HEIGHT / 2 - 50):self.fd(PADDLE_MOVE_DISTANCE)
        
    def Down(self):
        if self.ycor()>-(SCREEN_HEIGHT / 2 - 50):self.bk(PADDLE_MOVE_DISTANCE)
  
    def create_line(self):
        t = Turtle()
        t.width(5)
        t.speed("fastest")
        t.hideturtle()
        t.penup()
        t.goto(0,300)
        t.color("white")
        t.rt(90)
        for i in range(20):
            t.pendown()
            t.fd(20)
            t.penup()
            t.fd(10)
            
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color("white")
        self.x_move = [-1,1][randint(0,1)] * BALL_SPEED
        self.y_move = [-1,1][randint(0,1)] * BALL_SPEED
        
    def move(self):
        self.goto(self.xcor()+self.x_move,self.ycor()+self.y_move)
        
    def y_bounce(self):
        self.y_move *= -1
        
    def x_bounce(self):
        self.x_move *= -1
        
    def reset_position(self):
        self.goto(0,0)
        self.x_move = [-1,1][randint(0,1)] * BALL_SPEED
        self.y_move = [-1,1][randint(0,1)] * BALL_SPEED
        
class Score(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.width(5)
        self.goto(position)
        self.write("0",font = FONT)
        self.score = 0
    
    def add_score(self):
        self.clear()
        self.score += 1
        self.write(str(self.score),font = FONT)
        
def stop():
    global game_on
    game_on = False
               
screen = Screen()
screen.listen()
screen.title("Pong Game")
screen.setup(SCREEN_WIDTH,SCREEN_HEIGHT)
screen.bgcolor("black")
exit = Turtle()
exit.color("white")
exit.speed("fastest")
exit.hideturtle()
exit.penup()
exit.write("Press q to exit",align = "center",font = FONT)
time.sleep(2)
exit.clear()
screen.tracer(0)
paddle_1 = Paddle(positions[0])
paddle_2 = Paddle(positions[1])
ball = Ball()
screen.onkeypress(paddle_1.Up,'Up')
screen.onkeypress(paddle_1.Down,'Down')
screen.onkeypress(paddle_2.Up,'z')
screen.onkeypress(paddle_2.Down,'s')
screen.onkeypress(stop,'q')
score_1 = Score((-20-list(FONT)[1],SCREEN_HEIGHT/2 - 80))
score_2 = Score((20,SCREEN_HEIGHT/2 - 80))

flag = True
while game_on:
    screen.update()
    time.sleep(0.01)
    ball.move()
    if ball.ycor() >= SCREEN_HEIGHT/2 or ball.ycor() <= -SCREEN_HEIGHT/2:
        ball.y_bounce()
        
    if ((ball.distance(paddle_1) < 30 and ball.xcor() < -(SCREEN_WIDTH/2 - 60)) or (ball.distance(paddle_2) < 50 and ball.xcor() > (SCREEN_WIDTH/2 - 60))) and flag:
        ball.x_bounce()
        flag = False
        
    if not((ball.distance(paddle_1) < 30 and ball.xcor() < -(SCREEN_WIDTH/2 - 60)) or (ball.distance(paddle_2) < 50 and ball.xcor() > (SCREEN_WIDTH/2 - 60))) and flag != True:
        flag = True
        
    if ball.xcor() not in range(-SCREEN_WIDTH//2,SCREEN_WIDTH//2):
        if ball.xcor() < -SCREEN_WIDTH//2:score_2.add_score()
        else:score_1.add_score()
        ball.reset_position()
        screen.update()
        time.sleep(0.5)
screen.clear()
screen.bgcolor("black")
if score_1.score > score_2.score:exit.write("Player 1 wins",align = "center",font = FONT)
elif score_1.score < score_2.score:exit.write("Player 2 wins",align = "center",font = FONT)
else : exit.write("Draw",align = "center",font = FONT)
time.sleep(0.5)
screen.bye()