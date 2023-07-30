"""
File: 
Name:RAY
-------------------------
make a bouncing ball
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
count = 0
switch = True

window = GWindow(800, 500, title='bouncing_ball.py')


ball = GOval(SIZE, SIZE)
ball.filled = True
window.add(ball, START_X, START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(click)


def click(mouse):
    global switch
    global GRAVITY
    global VX
    global count
    if switch:
        vy = 0
        switch = False
        while True:
            vy += GRAVITY
            if ball.y + ball.height >= window.height:
                vy = -vy*REDUCE
                ball.move(VX, vy)
                pause(DELAY)
            else:
                ball.move(VX, vy)
                pause(DELAY)
            if ball.x + ball.height >= window.width:
                window.add(ball, START_X, START_Y)
                break
        count += 1
        print(count)
        if count < 3:
            switch = True
        else:
            switch = False


if __name__ == "__main__":
    main()
