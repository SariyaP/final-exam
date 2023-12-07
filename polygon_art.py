import turtle
import random


class Art:
    def __init__(self, choice: int):
        self.choice = choice
        self.random()
        if self.choice == 1:
            self.num_sides = 3
            for i in range(25):
                self.draw_polygon()
                self.random()
        if self.choice == 5:
            self.num_sides = 3
            for i in range(25):
                self.draw_polygon()
                for i in range(3):
                    self.draw_inside()
                self.random()
        if self.choice == 2:
            self.num_sides = 4
            for i in range(25):
                self.draw_polygon()
                self.random()
        if self.choice == 6:
            self.num_sides = 4
            for i in range(25):
                self.draw_polygon()
                for i in range(3):
                    self.draw_inside()
                self.random()
        if self.choice == 3:
            self.num_sides = 5
            for i in range(25):
                self.draw_polygon()
                self.random()
        if self.choice == 7:
            self.num_sides = 5
            for i in range(25):
                self.draw_polygon()
                for i in range(3):
                    self.draw_inside()
                self.random()
        if self.choice == 4:
            for i in range(25):
                self.num_sides = random.randint(3, 5)
                self.draw_polygon()
                self.random()
        if self.choice == 8:
            for i in range(25):
                self.num_sides = random.randint(3, 5)
                self.draw_polygon()
                for i in range(3):
                    self.draw_inside()
                self.random()

    def random(self):
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = self.get_new_color()
        self.size = random.randint(50, 150)
        self.border_size = random.randint(1, 10)
        self.reduction_ratio = 0.618

    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw_polygon(self):
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
    def draw_inside(self):
        turtle.penup()
        turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]
        self.size *= self.reduction_ratio
        self.draw_polygon()
        turtle.penup()



num = int(input("Which art do you want to generate? "
            "Enter a number between 1 to 8,inclusive: "))
turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)
newart = Art(num)
turtle.done()