import turtle 
import random 
import pygame 

delay = 0.1 
score = 0 
high_score = 0 

pygame.mixer.init() 
bite_sound = pygame.mixer.Sound("apple-bite-316785.wav") 
bite_sound.set_volume(1.0) 

wn = turtle.Screen() 
wn.title("Snake Game by @lovedino") 
wn.bgcolor("lightgreen") 
wn.setup(width=600, height=600)
wn.tracer(0) 

head = turtle.Turtle() 
head.speed(0) 
head.shape("square") 
head.color("blue") 
head.penup() 
head.goto(0, 0) 
head.direction="stop"

# Apple 

food = turtle.Turtle() 
food.speed(0) 
food.shape("circle") 
food.color("red") 
food.penup() 
food.goto(0, 100) 

segments = [] 

pen = turtle.Turtle() 
pen.speed(0) 
pen.shape("square") 
pen.color("black") 
pen.penup() 
pen.hideturtle() 
pen.goto(0, 260) 
pen.write("score : 0, high score : 0", align = "center", font = ("Courier", 24, "normal")) 

# Functions 

def go_up(): 
    if head.direction != "down": 
        head.direction = "up" 
def go_down(): 
    if head.direction != "up": 
        head.direction = "down" 
def go_left(): 
    if head.direction != "right": 
        head.direction = "left" 
def go_right(): 
    if head.direction != "left": 
        head.direction = "right" 
        
def move(): 
    step = 20 

    for i in range(len(segments)-1, 0, -1): 
        x = segments[i-1].xcor() 
        y = segments[i-1].ycor() 
        segments[i].goto(x, y) 
        
    if len(segments) > 0: 
        segments[0].goto(head.xcor(), head.ycor()) 

    if head.direction == "up": 
        head.sety(head.ycor() + step) 
    if head.direction == "down": 
        head.sety(head.ycor() - step) 
    if head.direction == "left": 
        head.setx(head.xcor() - step) 
    if head.direction == "right":
         head.setx(head.xcor() + step) 
         

def game_reset():
    global score, high_score, delay
    head.goto(0, 0) 
    head.direction = "stop"

    for segment in segments:
        segment.goto(1000, 1000) 

    segments.clear() 
    score = 0 
    delay = 0.1 
    pen.clear() 
    pen.write(f"score : {score} , high score : {high_score}", align = "center", font = ("Courier", 24, "normal"))
        
def game_loop(): 
    wn.update() 
    global delay, score, high_score 

    move()
            
    if head.distance(food) < 20: 
        x = random.randint(-290, 290) 
        y = random.randint(-290, 290) 
        food.goto(x, y) 
        new_segment = turtle.Turtle() 
        new_segment.speed(0) 
        new_segment.shape("square")
        new_segment.color("darkblue") 
        new_segment.penup() 
        
        if segments: 
            last_seg = segments[-1] 
            new_segment.goto(last_seg.xcor(), last_seg.ycor()) 
        else: 
            new_segment.goto(head.xcor(), head.ycor()) 
        
        segments.append(new_segment) 
            
        bite_sound.play() 
        score += 10 
        if score > high_score: 
            high_score = score 
        delay -= 0.001  
        pen.clear() 
        pen.write(f"score : {score} , high score : {high_score}", align = "center", font = ("Courier", 24, "normal")) 

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        game_reset()
            
    for segment in segments[:-1]: 
        if segment.distance(head) < 20: 
            game_reset()
            break
    
    wn.ontimer(game_loop, int(delay * 1000)) 
    
    
wn.listen() 
wn.onkeypress(go_up, "w") 
wn.onkeypress(go_down, "s") 
wn.onkeypress(go_left, "a") 
wn.onkeypress(go_right, "d")

game_loop() 
wn.mainloop()