import turtle

t = turtle.Turtle()

t.hideturtle()
turtle.tracer(0, 0)

window = turtle.Screen()
window.bgcolor('#FBEEDE')

# Move template
def move(z, h):
    t.penup()
    t.goto(z, h)
    t.pendown()

# Square template
def t_square(x):
     for i in range(4):
        t.forward(x)
        t.right(90)

# Circle template
def t_circle(r):
    for i in range(360):
        t.forward(r)
        t.left(1)

# Rectangle template
def t_rectangle(h, v, a):
    for i in range(2):
        t.forward(h)
        t.right(a)
        t.forward(v)
        t.right(a)

# Semicircle template
def t_semi(h):
    t.left(90)
    for x in range(180):
        t.forward(h)
        t.right(1)
    t.right(90)
    t.forward(57.5)

# Start Coloring
def color_init(s):
    t.penup()
    t.fillcolor(s)
    t.begin_fill()

# Common Rectangles in the program
def rec_features(x, y, h, w, a):
    move(x, y)
    t_rectangle(h, w, a)

# Common Squares in the program
def sqr_features(x, y, h):
     move(x, y)
     t_square(h)

# Common Circles in the program
def circle_features(x, y, r):
    move(x, y)
    t_circle(r)

# Antena
def antena():
    # Circle antena
    color_init('#C85035')
    circle_features(0, 160, 0.19)
    t.end_fill()
    
    # Rectangle antena
    color_init('#3A3934')
    rec_features(-1.7, 160, 4, 20, 90)
    t.end_fill()

    # Semicircle antena
    color_init('#488BA6')
    move(-28, 110)
    t_semi(0.5)
    t.end_fill()

# Eye template
def eye(x, y, r):
    circle_features(x, y, r)

# Drawing eyes
def eyes():
    color_init('#C85035')    
    eye(20, 90, 0.2)
    t.end_fill()

    color_init('#C85035')
    eye(-20, 90, 0.2)
    t.end_fill()

# Ear template
def ear(x, y, h, w, a):
    rec_features(x, y, h, w, a)

# Drawing ears
def ears():
    color_init('#488BA6')
    ear(56, 45, 10, 50, 90)
    t.end_fill()

    color_init('#488BA6')
    ear(-44, 45, 10, 50, 90)
    t.end_fill()

# Mouth template
def mouth(x, y, h, w, a):
    rec_features(x, y, h, w, a)
    
# Head | Putting all features together
def head():
    color_init('#79A9B7')
    sqr_features(-44, 110, -90)
    t.end_fill()
    
    eyes()

    # Drawing mouth
    color_init('#C85035')    
    mouth(30, 35, 60, 10, 90)
    t.end_fill()

    ears()

# Neck
def neck():
    color_init('#878684')
    rec_features(-20, 20, -40, -10, 90)
    t.end_fill()
    
    color_init('#878684')
    rec_features(-20, 10, -40, -10, 90)
    t.end_fill()
    
# Body
def body():
    # Body Rectangle
    color_init('#488BA6')
    sqr_features(75, -150, 150)
    t.end_fill()

    # Interior Square
    color_init('#79A9B7')
    sqr_features(60, -105, 90)
    t.end_fill()

    # Circle Btn
    color_init('#79A9B7')
    move (-50, -115)
    t_circle(0.15)
    t.end_fill()

# Arm part template
def arm_part(x, y, h, w, a):
    rec_features(x, y, h, w, a)

# Arm template
def arm(x, y, h, w, a):
    color_init('#7F7A76')
    arm_part(x, y, h, w, a)
    t.end_fill()

# Choosing between the right and left arm based on current cordinates
    if x >= 0:
        color_init('#5B5653')
        arm_part(x, y - 5, -h, w + 10, a)
        t.end_fill()

        color_init('#7F7A76')
        arm_part(x + 50, y, -h + 40, w, a)
        t.end_fill()
    else:
        color_init('#5B5653')
        arm_part(x - 100, y - 5, -h, w + 10, a)
        t.end_fill()
        
        color_init('#7F7A76')
        arm_part(x - 110, y, -h + 40, w, a)
        t.end_fill()

# Drawing Arms
def arms():
    arm(125, -40, 50, 20, 90)
    arm(-75, -40, 50, 20, 90)

# Leg part template
def leg_part(x, y, h, w, a):
    rec_features(x, y, h, w, a)

# Leg template
def leg(x, y, h, w, a):
    color_init('#7F7A76') 
    leg_part(x, y, h, w, a)
    t.end_fill()

# Choosing between the right and left arm based on current cordinates
    if x >= 0:
        color_init('#5B5653')
        leg_part(x, y - 35, h, w + 80, a)
        t.end_fill()
        
        color_init('#5B5653')
        leg_part(x + 5, y - 90, h + 10, w + 75, a)
        t.end_fill()
    else:
        color_init('#5B5653')
        leg_part(x, y - 35, h, w + 80, a)
        t.end_fill()
        
        color_init('#5B5653')
        leg_part(x + 5, y - 90, h + 10, w + 75, a)
        t.end_fill()

# Drawing legs
def legs():
    leg(55, -150, 40, -90, 90)
    leg(-15, -150, 40, -90, 90)

# Joined Robot Parts
def complete_robot():
    antena()
    head()
    neck()
    body()
    arms()
    legs()

complete_robot()

turtle.update()

window.exitonclick()

