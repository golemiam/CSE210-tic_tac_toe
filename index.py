'''
Project Name:  Prove assignment: Tic Tac Toe
Author: Robbie Platt
Due Date: 2022-09-23
Course: Tic Tac Toe

For this assignment I will create a tic tac toe game using turtle imaging, The person will select
a position and the turtle will draw a new grid for each placement of the tic tac toe play. Circle gets
to choose their color, x gets to go first. (Benefit of going second is to get to choose your color).
After 9 turns the game will end automatically, however if you wish to be done sooner you may quit at any
time, and restart if you want by running the program again.
'''

import turtle

def main(scale):
    """
    Main program
    """
    _t = turtle.Turtle()
    _s = turtle.getscreen()
    _s.bgcolor("sky blue")
    draw_grid(_t)
    #winning_status = 0
    try:
        turn_countdown = 9
        while turn_countdown > 0:
      
            x_turn(_t, -45, 75)
            turn_countdown -= 1
            
            if turn_countdown > 0:
                o_turn(_t)
                turn_countdown -= 1
    except:
        print("""
        for columns and rows, please input only 1,2, or 3 without any spaces, or other numbers.
        for choosing a color, it must be a valid color name within the python library. If you chose a
        fancy color name and it did not work, try being a little more boring.""")
    print("I hope you enjoyed playing, have a nice day")


def o_turn(_t):
    """
    positions the o, and obtains the color from the user.
    """
    column = input("Please select a column by typing the corresponding number: 1, 2, or 3: ")
    row = input("Please select a row by typing the corresponding number: 1, 0, or -1: ")
    size = 25
    radius = size
    color = input("What color would you like your circle?: ")
    pencolor = str(color)
    fillcolor = "skyblue"
    _x = int(column) * 50 - 57
    _y = (int(row) - 2) * 50 + 6
    draw_circle(_t, _x, _y, radius, fillcolor, pencolor)
    
def draw_circle(_t, _x, _y, radius, fillcolor, pencolor):
    """
    _x, and _y are for coordinates
    radius is used for the circle size
    fillcolor is for the color inside of the circles
    pencolor is for the circle borders
    """
    _t.color(pencolor, fillcolor)
    _t.begin_fill()
    _t.up()
    _t.goto(_x,_y)
    _t.down()
    _t.circle(radius)
    _t.end_fill()
    _t.speed(0)
    
def x_turn(_t, tilt, length):
    """
    positions the x
    """
    column = input("Please select a column by typing the corresponding number: 1, 2, or 3: ")
    row = input("Please select a row by typing the corresponding number: 1, 2, or 3: ")
    _x = int(column) * 50
    _y= (int(row) - 2) * 50
    _t.up()
    _t.goto(_x - 100, _y + 50)

    _t.down()
    _t.setheading(tilt)
    _t.forward(length)
    _t.up()    
    _t.goto( (_x - 100), (_y))

    _t.down()
    _t.setheading(tilt + 90)
    _t.forward(length)
    _t.up()
    

def draw_grid(_t):
    """
    Draws the playing area.
    """
    draw_vertical_line(_t, 50, -50, 90, 150)
    draw_vertical_line(_t, 0, -50, 90, 150)
    draw_horizontal_line(_t, -50, 50, 0, 150)
    draw_horizontal_line(_t, -50, 0, 0, 150)
    
def draw_vertical_line(_t, _x, _y, tilt, length):
    """
    Creates a veritical line, used for grid.
    """
    _t.up()
    _t.goto(_x, _y)

    _t.down()
    _t.setheading(tilt)
    _t.forward(length)
    _t.up()

def draw_horizontal_line(_t, _x, _y, tilt, length):
    """
    Creates a horizontal line, used for grid.
    """
    _t.up()
    _t.goto(_x, _y)

    _t.down()
    _t.setheading(tilt)
    _t.forward(length)
    _t.up()

if __name__== "__main__":
    scale = 1.0
    main(scale)
    """
    scale not used.
    """
