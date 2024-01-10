import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle Game")
FONT = ("Arial", 15, "normal")
score = 0       # score'u bir değişken olarak atıyorum ki değiştirebileyim
time = 30
game_over = False

turtle_list = []        #turtle'ları gizlemek için boş liste
score_turtle = turtle.Turtle()
def set_up_score_turtle():
    score_turtle.color("dark blue")
    score_turtle.penup()
    score_turtle.hideturtle()

    # ekranın yüksekliğinin yarısı lazım bana
    top_height = screen.window_height() / 2
    y_value = top_height * 0.9

    score_turtle.setpos(x=0, y= y_value)
    score_turtle.write(arg= "Score: 0", move=False, align="center", font=FONT)

grid_size = 10

def make_turtle(x,y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=FONT)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(1.5,1.5)
    t.color("green")
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)


x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [-20, -10, 0, 10, 20]

def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

def show_turtle_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()     #choice random'un bir methodu
        screen.ontimer(show_turtle_randomly, 500)

countdown_turtle = turtle.Turtle()
def countdown(time):
    global game_over
    countdown_turtle.penup()
    countdown_turtle.hideturtle()

    # ekranın yüksekliğinin yarısı lazım bana
    top_height = screen.window_height() / 2
    y_value = top_height * 0.9

    countdown_turtle.setpos(x=0, y=y_value - 30)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)      #1000 milisaniye = 1 saniye
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over", move=False, align="center", font=FONT)


turtle.tracer(0)       #bu ve sondaki setup aşamasındaki animasyonları atlamamızı sağlıyor

set_up_score_turtle()
setup_turtles()
hide_turtles()
show_turtle_randomly()
countdown(10)

turtle.tracer(1)

turtle.mainloop()