import turtle

x = 0
y = 0
pen = None
screen = None
fill_color = 'pink'

# Place the hidden object randomly on the screen
# It will begin in the center of the screen

# User determines difficulty of game by controlling size

# Change the objects color depending on whether they are hotter or colder

# Notify them how many moves they made to find the hidden object

# key listeners: s = hidden object H = hides the object R = reset the game


def move_home():
    """
    Reset the x and y back to zero coordinate which will be used position the circle in the center
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global x, y
    x = 0  # center of screen moving right or left
    y = 0  # center of screen moving up or down
    draw_circle()


def move_up():
    """
    Add 20 to the y coordinate which will be used move the circle up
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global y
    y += 20  # move top of center
    draw_circle()


def move_down():
    """
    Subtract 20 from y coordinate which will be used move the circle to the down
    then call draw_circle to clear & redraw the circle is on the screen based on its new location
    Returns:
        None
    """

    global y
    y -= 20  # move down of center
    draw_circle()


def move_right():
    """
    Add 20 to the x coordinate which will be used move the circle to the right
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global x
    x += 20  # move to the right of center
    draw_circle()


def move_left():
    """
    Subtract 20 from the x coordinate which will be used move the circle to the left
    then call draw_circle to clear & redraw the circle is on the screen based on its new location

    Returns:
        None
    """

    global x
    x -= 20  # move to the left of center
    draw_circle()


def draw_circle(diameter=10):
    """
    clear the screen and draw the circle based on the x & y coordinates

    Args:
        diameter (int): the diameter size of the circle (default 10)
        fill_color (str): the inside color of the circle (default red)

    Returns:
        None
        :param pen: Turtle which the user controls
    """

    global x, y, fill_color

    pen.hideturtle()  # don't show the icon
    pen.speed('fastest')  # draw quickly

    pen.clear()  # clear the previous screen for the update circle location

    # write text on the screen
    pen.penup()  # don't want to see icon moving on the screen
    pen.goto(-350, 350)  # from the current position which is center after clear, move left 350 up 350
    pen.pencolor('white')  # text color
    pen.write("Use arrows to move, or press 'h' for home", font=("Verdana", 12, "bold"))

    # draw circle
    pen.goto(x, y)  # move to the updated x (left-right) and y (up-down) location from center
    pen.pendown()  # start drawing the outline of the circle
    pen.fillcolor(fill_color)  # fill color of the circle
    pen.begin_fill()  # start the fill of whatever is being drawn
    pen.circle(50)  # diameter of the circle
    pen.end_fill()  # done drawing the object to complete the fill


def setup_window(bg_color='white'):
    """
    Controls how the window looks.

    Args:
        bg_color (str): the background color of the window (default white)

    Returns:
        None
    """
    screen.tracer(False)  # turn animation off which causes screen flickering as the circle gets redrawn

    # pen.screen.tracer(False)
    screen.title('Moving Circle')  # title the title bar of the window
    screen.bgcolor(bg_color)  # set the window's background color
    screen.setup(800, 900)  # the size of the window

    # set up the keys to listen to and what function should be called
    screen.onkeypress(move_home, "h")
    screen.onkeypress(move_up, "Up")
    screen.onkeypress(move_down, "Down")
    screen.onkeypress(move_right, "Right")
    screen.onkeypress(move_left, "Left")
    screen.listen()  # start listening for keys being pressed


def main():
    """
    The main function, used to test drawing a square

    Returns:
        None
    """
    setup_window('black')
    draw_circle(50)
    turtle.mainloop()


# if this is the program starting module, then run the main function
if __name__ == '__main__':
    screen = turtle.Screen()
    pen = turtle.Turtle()
    main()
