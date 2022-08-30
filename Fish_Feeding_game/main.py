import turtle as t
import random as rd

t.bgcolor('blue')

#fish shape,color, speed
fish = t.Turtle()
fish.shape('arrow')
fish.color('orange')
fish.speed(0)
fish.penup()
fish.hideturtle()

#food shape, color , speed
food = t.Turtle()
food.shape('circle')
food.color('white')
food.penup()
food.hideturtle()
food.speed()

game_started = False
text_turtle = False
text_turtle = t.Turtle()
text_turtle.write('Press SPACE to start', align='center', font=('Poppins', 18, 'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

#draw window
def outside_window():
    left_wall = -t.window_width()/2
    right_Wall = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2
    (x,y) = fish.pos()
    outside = x < left_wall or x > right_Wall or y > top_wall or y < bottom_wall
    return outside

#game over 
def game_over():
    fish.color('red')
    food.color('red')
    t.penup()
    t.hideturtle()
    t.color('Orange')
    t.write('GAME OVER !', align='center', font=('Poppins', 30, 'bold',))

#display score and x, y place in middle
def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    score_turtle.color('white')
    x = (t.window_width()/2) - 70
    y = (t.window_height()/2) - 70
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score), align='right', font=('Poppins', 40, 'bold'))

#food place
def place_food():
    food.hideturtle()
    food.setx(rd.randint(-200,200))
    food.sety(rd.randint(-200,200))
    food.showturtle()

#game start function
def start_game():
    global game_started
    if game_started:
        return
    game_started = True

    score = 0
    text_turtle.clear()   

    fish_speed = 2
    fish_length = 1
    fish.shapesize(1,fish_length,1)
    fish.showturtle()
    display_score(score)
    place_food()   

    while True:
        fish.forward(fish_speed)
        if fish.distance(food) < 20:
            place_food()
            fish_length = fish_length + 1
            fish.shapesize(1,fish_length,1)
            fish_speed = fish_speed + 1
            score = score + 10
            display_score(score)
        if outside_window():
            game_over()
            break

def move_up():
    if fish.heading() == 0 or fish.heading() == 180:
        fish.setheading(90)

def move_down():
    if fish.heading() == 0 or fish.heading() == 180:
        fish.setheading(270)

def move_left():
    if fish.heading() == 90 or fish.heading() == 270:
        fish.setheading(180)

def move_right():
    if fish.heading() == 90 or fish.heading() == 270:
        fish.setheading(0)

#keys
t.onkey(start_game, 'space')
t.onkey(move_up, 'Up')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')
t.onkey(move_right, 'Right')
t.listen()
t.mainloop()

