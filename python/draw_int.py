import turtle 
import random

ball_size = 20
player_size = 20

# objects

wn = turtle.Screen()
wn.setup(600, 600)
wn.title("Number Game by @lovedino")
wn.tracer(0)
wn.bgcolor("white")

player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.penup()
player.goto(0, 0)

number = turtle.textinput("정수 입력", "정수 입력 : ")
balls = []
location = []

for digit in number :
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("white")
    ball.pencolor("black")
    ball.penup()

    # random location

    while True :
        x = random.randint(-300 + ball_size, 300 - ball_size)
        y = random.randint(-300 + ball_size, 300 - ball_size)
        bull = False
        for lx, ly in location :
            if x == lx and y == ly :
                bull = True
                break

        if not bull :
            break

    
    ball.goto(x, y)
    ball.write(digit, align = "center", font = ("Arial", 12, "bold"))
    balls.append((ball, digit))
    location.append((x, y))


# functions

def go_up():
    player.sety(player.ycor() + 20)

def go_down():
    player.sety(player.ycor() - 20)

def go_left():
    player.setx(player.xcor() - 20)

def go_right():
    player.setx(player.xcor() + 20)

number_index = 0

def game_loop():
    global number_index
    wn.update()
    if number_index < len(balls) :
        ball, digit = balls[number_index]
        if player.distance(ball) < ball_size :
            ball.clear()
            ball.hideturtle()
            number_index += 1
    else : 
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        pen.goto(0, 0)
        pen.write(f"{number}", align = "center", font = ("Arial", 40, "bold"))
        return
    
    wn.ontimer(game_loop, 50)



wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

game_loop()
wn.mainloop()
