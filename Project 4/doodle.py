import sys
import turtle

def main():

    tur = turtle
    # Get user input and validate
    while True:
        try:
            if len(sys.argv) != 2:
                raise Exception(print("""
            Unexpected number of parameters given.
            Format: python3 [scriptfile.py {1,2,3}]"""))
            elif ".py" not in sys.argv[0]:
                raise Exception(print("""
            Please enter a valid .py 
            file or check your path."""))
            elif 0 > int(sys.argv[1]) > 3:
                raise Exception(print("Please enter 1, 2, or 3"))
            modifier = int(sys.argv[1])
            break
        except TypeError:
            print("Unexpected input type received. Please try again")
            quit()
        except:
            print("Unexpected input. Please try again.")
            quit()

    mod_1 = [0, 200, 150, 15, 50]
    mod_2 = [0, 100, 200, 240, 50]
    mod_3 = [[100, 100, 75, 7.5, 25], [-100, 50, 100, 120, 25]]

    
    def draw_circle(color, size):
        '''
        Draw circle of specified color and size
        '''
        tur.color(color)  # Param passes into color
        tur.begin_fill()  # Shape will be filled in with chosen color
        tur.circle(size) # Draws circle to length param
        tur.end_fill()    # Shape has been filled with the color

    
    def draw_triangle(color, leng):
        '''
        Draw triangle of specified color and side length
        '''
        tur.color(color)
        tur.begin_fill()
        for ele in range(3): # Draws the triangle to length param
            tur.fd(leng)
            tur.lt(120)
        tur.end_fill()


    def draw_rect(color, width, height):
        '''
        Draw rectangle of specified color, height, width
        '''
        tur.color(color)
        tur.begin_fill()
        counter = 0
        while counter < 2:
            tur.fd(width)
            tur.lt(90)
            tur.fd(height)
            tur.lt(90)
            counter += 1
        tur.end_fill()

    def placement(x_cor, y_cor=0):
        '''
        Place the turtle in a specified spot, facing east
        '''
        tur.up()
        tur.setx(x_cor)
        tur.sety(y_cor)
        tur.down()
        tur.heading()
    
    def build_house(offset, house_l, house_h, window, door):
        placement(offset)
        draw_rect('gray', house_l, house_h)     # House body
        placement(offset - (house_l * .05), house_h)
        draw_triangle('red', house_l * 1.1)     # Roof
        placement(offset + (house_l * .4)) 
        draw_rect('red', door, door * 2)        # Door
        placement(offset + (door * .4) + (house_l / 2), (door * .9))
        draw_circle('yellow', window / 5)       # Door knob
        placement(offset + (house_l * .2), house_h * .6)
        draw_circle('yellow', window)           # Window 1
        placement(offset + (house_l * .8), house_h * .6)
        draw_circle('yellow', window)           # Window 2
        placement(offset + (house_l * .75), house_h)
        draw_rect('red', door / 3, door * 3)    # Chimney
        for ele in range(0, 30, 10):
            placement(offset + (house_l * .8 + ele), house_h + ele + door * 3.3)
            draw_circle('black', window)         # Smoke clouds
        
    def grow_tree(offset, base, trunk, branch, leaf):
        placement(offset)
        draw_triangle('brown', base)                # Tree base
        placement(offset + (base * .2))
        draw_rect('brown', base * .6, trunk)        # Tree trunk
        placement(offset - branch * .3, trunk * .8)
        draw_rect('brown', branch, branch * .05)    # Horizontal branches
        placement(offset + base / 2 - branch * .025 , trunk / 3)
        draw_rect('brown', branch * .05, branch)    # Vertical branch
        placement(offset - branch / 3, trunk * .6)
        draw_circle('green', leaf)                  # Leaf 1
        placement(offset + base + branch / 3, trunk * .6)
        draw_circle('green', leaf)                  # Leaf 2
        placement(offset + base / 2, trunk + branch * .3)
        draw_circle('green', leaf * 1.5)            # Leaf 3

    if modifier == 1:
        build_house(*mod_1)
    elif modifier == 2:
        grow_tree(*mod_2)
    elif modifier == 3:
        build_house(*mod_3[0])
        grow_tree(*mod_3[1])
    else:
        print("How did you do that?! There's nothing here!")


if __name__ == "__main__":
    main()
    turtle.done()
