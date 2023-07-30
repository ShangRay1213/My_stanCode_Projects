"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics


FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3		# Number of attempts

graphics = BreakoutGraphics()


def main():

    # Add the animation loop here!
    dx = graphics.dx() # __dx
    dy = graphics.dy() # __dy
    ball_radius = graphics.ball_radius()
    switch = True
    for i in range(NUM_LIVES):
        if graphics.count2 == graphics.count:
            break
        while graphics.ball.y < graphics.window.height:
            if graphics.count2 == graphics.count:
                break
            while dx == 0 and dy == 0:
                dx = graphics.dx() # __dx
                dy = graphics.dy() # __dy
                pause(40)
            graphics.ball.move(dx, dy)
            pause(FRAME_RATE)
            if graphics.ball.x >= graphics.window.width or graphics.ball.x <= 0:
                dx = -dx
            if graphics.ball.y <= 0:
                dy = -dy
            obj = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
            obj2 = graphics.window.get_object_at(graphics.ball.x + 2 * ball_radius, graphics.ball.y)
            obj3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + 2 * ball_radius)
            obj4 = graphics.window.get_object_at(graphics.ball.x + 2 * ball_radius, graphics.ball.y + 2 * ball_radius)
            if obj is not None and obj != graphics.paddle:
                graphics.window.remove(obj)
                dy = -dy
                graphics.count2 += 1
                switch = True
            elif obj2 is not None and obj2 != graphics.paddle:
                graphics.window.remove(obj2)
                dy = -dy
                graphics.count2 += 1
                switch = True
            elif obj3 is not None and obj3 != graphics.paddle:
                graphics.window.remove(obj3)
                dy = -dy
                graphics.count2 += 1
                switch = True
            elif obj4 is not None and obj4 != graphics.paddle:
                graphics.window.remove(obj4)
                dy = -dy
                graphics.count2 += 1
                switch = True
            elif obj == graphics.paddle or obj2 == graphics.paddle or obj3 == graphics.paddle or obj4 == graphics.paddle:
                if switch:
                    dy = -dy
                    switch = False
        graphics.window.add(graphics.ball, x=(graphics.window.width - ball_radius) / 2,
                            y=(graphics.window.height - ball_radius) / 2)
        graphics.set_dx()
        graphics.set_dy()
        dx = 0
        dy = 0
    print(NUM_LIVES)


if __name__ == '__main__':
    main()
