"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random
from campy.gui.events.timer import pause

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10      # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 80     # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width - paddle_width) / 2,
                    y=window_height - paddle_offset)
        self.window.add(self.paddle)
        self.switch = True
        self.paddle.filled = True

        # Center a filled ball in the graphical window

        self.ball = GOval(ball_radius, ball_radius, x=(window_width-ball_radius)/2, y=(window_height-ball_radius)/2)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.radius = ball_radius

        # Initialize our mouse listeners
        onmouseclicked(self.move_set)
        onmousemoved(self.p)

        # Count how many left
        self.count = brick_cols*brick_rows
        self.count2 = 0

        # Draw bricks
        brick_x = 0
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if i < brick_cols/5:
                    self.brick.fill_color = "red"
                elif brick_cols/5 <= i < (brick_cols/5)*2:
                    self.brick.fill_color = "orange"
                elif (brick_cols / 5) * 2 <= i < (brick_cols / 5) * 3:
                    self.brick.fill_color = "yellow"
                elif (brick_cols / 5) * 3 <= i < (brick_cols / 5) * 4:
                    self.brick.fill_color = "green"
                elif (brick_cols / 5) * 4 <= i < (brick_cols / 5) * 5:
                    self.brick.fill_color = "blue"
                if j == 0:
                    self.window.add(self.brick, x=0, y=brick_offset+(brick_spacing + brick_height)*i)
                else:
                    self.window.add(self.brick, x=brick_x + (brick_spacing+brick_width), y=brick_offset+(brick_spacing +
                    brick_height)*i)
                    brick_x += (brick_spacing+brick_width)
                    if j == brick_rows-1:
                        brick_x = 0


    def p(self, event):
        if event.x + (self.paddle.width / 2) >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        elif event.x - (self.paddle.width / 2) <= 0:
            self.paddle.x = 0
        else:
            self.paddle.x = event.x - self.paddle.width / 2

    def move_set(self, event):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx
        if self.ball.y > self.window.height:
            self.__dx = 0
            self.__dy = 0

    def dx(self):
        return self.__dx

    def dy(self):
        return self.__dy

    def ball_radius(self):
        return self.radius

    def set_dx(self):
        self.__dx = 0

    def set_dy(self):
        self.__dy = 0








