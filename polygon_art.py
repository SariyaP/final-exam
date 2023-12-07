import turtle
import random

def draw_polygon(num_sides, size, orientation, location, color, border_size):
    turtle.penup()
    turtle.goto(location[0], location[1])
    turtle.setheading(orientation)
    turtle.color(color)
    turtle.pensize(border_size)
    turtle.pendown()
    for _ in range(num_sides):
        turtle.forward(size)
        turtle.left(360/num_sides)
    turtle.penup()

def get_new_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))



# # draw a polygon at a random location, orientation, color, and border line thickness
# num_sides = random.randint(3, 5) # triangle, square, or pentagon
# size = random.randint(50, 150)
# orientation = random.randint(0, 90)
# location = [random.randint(-300, 300), random.randint(-200, 200)]
# color = get_new_color()
# border_size = random.randint(1, 10)
# draw_polygon(num_sides, size, orientation, location, color, border_size)
#
# # specify a reduction ratio to draw a smaller polygon inside the one above
# reduction_ratio = 0.618
#
# # reposition the turtle and get a new location
# turtle.penup()
# turtle.forward(size*(1-reduction_ratio)/2)
# turtle.left(90)
# turtle.forward(size*(1-reduction_ratio)/2)
# turtle.right(90)
# location[0] = turtle.pos()[0]
# location[1] = turtle.pos()[1]
#
# # adjust the size according to the reduction ratio
# size *= reduction_ratio
#
# # draw the second polygon embedded inside the original
# draw_polygon(num_sides, size, orientation, location, color, border_size)
#
# # hold the window; close it by clicking the window close 'x' mark
# turtle.done()
class Art:
    def __init__(self, choice:int):
        self.choice = choice
        self.random()
        if self.choice == 1:
            self.num_sides = 3
            for i in range(25):
                draw_polygon(self.num_sides, self.size, self.orientation, self.location, self.color, self.border_size)
                self.random()
        if self.choice == 5:
            self.num_sides = 3
            for i in range(25):
                draw_polygon(self.num_sides, self.size, self.orientation, self.location, self.color, self.border_size)
                self.random()
                self.draw_inside()
        if self.choice == 2 or self.choice == 6:
            self.num_sides = 4
        if self.choice == 3 or self.choice == 7:
            self.num_sides = 5
        if self.choice == 4 or self.choice == 8:
            self.num_sides = random.randint(3, 5)

    def random(self):
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = get_new_color()
        self.size = random.randint(50, 150)
        self.border_size = random.randint(1, 10)
        self.reduction_ratio = 0.618

    def draw_inside(self):
        turtle.penup()
        turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]
        self.size *= self.reduction_ratio
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()
        draw_polygon(self.num_sides, self.size, self.orientation, self.location, self.color, self.border_size)

    def get_new_color(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


num = int(input("Which art do you want to generate? "
            "Enter a number between 1 to 8,inclusive: "))
turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)
newart = Art(num)
turtle.done()