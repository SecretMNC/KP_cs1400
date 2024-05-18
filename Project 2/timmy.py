import turtle as t
import random

# Define main function
def main():
    print("Timmy has begun making shapes!")

# Set conditional activation of main function
if __name__ == "__main__":
    main()
else:
    print("Timmy is visiting you and making you shapes!")

# List of 8 possible colors, randomly pick a color
def rand_color():
    color_list = ['red', 'orange', 'pink', 'green', 'blue', 'purple', 'black']
    return random.choice(color_list)

# Draw circle of random size and color, increment circle_counter
def draw_circle():
    draw_length = round(random.uniform(5, 200), 2) # Random size
    t.color(rand_color()) # Random color
    t.begin_fill()        # Shape will be filled in with chosen color
    t.circle(draw_length) # Actually draw the circle
    t.end_fill()          # Shape has been filled with the color
    global circle_counter # Grab global variable
    circle_counter += 1   # Increment that variable outside function's scope

# Draw triangle of random size and color, increment triangle_counter
def draw_triangle():
    draw_length = round(random.uniform(10, 400), 2)
    t.color(rand_color())
    t.begin_fill()
    for i in range(3): # Draws the triangle
        t.fd(draw_length)
        t.lt(120)
    t.end_fill()
    global triangle_counter
    triangle_counter += 1

# Draw square of random size and color, increment square_counter
def draw_square():
    draw_length = round(random.uniform(10, 400), 2)
    t.color(rand_color())
    t.begin_fill()
    counter = 0
    while counter < 4: # Draws the square
        t.fd(draw_length)
        t.lt(90)
        counter += 1
    t.end_fill()
    global square_counter
    square_counter += 1


# Place the turtle in a random spot
def rand_placement():
    t.penup()
    t.setx(round(random.uniform(-500, 500), 2))
    t.sety(round(random.uniform(-500, 500), 2))
    t.pendown()

# Randomly pick a shape to draw
def rand_basic_shape():
    shapes = [draw_circle, draw_triangle, draw_square]
    return shapes[random.randint(0,2)]()

# Guarrentess project requirements will be met despite randomness
def safety_check():
    check = shape_counter >= 10 and circle_counter > 0 and triangle_counter > 0 and square_counter > 0
    return check

# Declare shape counters
shape_counter = 0
circle_counter = 0
triangle_counter = 0
square_counter = 0

# Turtle draws a random number of shapes, minimum of 10
# At least one of each shape is drawn
while True:
    rng = random.randint(1, 100)
    if rng <= 95:                               # 95% chance a new shape gets drawn
        rand_placement()                        # Places turtle in random location
        rand_basic_shape()                      # Picks a random shape to draw
        shape_counter += 1                      # Increments the shape_counter
        print(f"Shapes drawn: {shape_counter}") # Tells user the shape count
    elif rng > 95 and safety_check() == False:  # 5% chance unless conditions aren't met
        continue
    else:
        print(f"""Timmy made...
{circle_counter} circles, 
{triangle_counter} triangles, and 
{square_counter} squares 
for a total of {shape_counter} shapes!""")
        break


t.mainloop()
