from tkinter import*
from random import randint
import socket

GRADUATION = 40
PIXEL = 10
STEP = 2 * PIXEL
WD = PIXEL * GRADUATION
HT = PIXEL * GRADUATION

OB_SIZE_FACTOR = 1
SN_SIZE_FACTOR = 0.9
OB_SIZE = PIXEL * OB_SIZE_FACTOR
SN_SIZE = PIXEL * SN_SIZE_FACTOR

BG_COLOR = 'black'
OB_COLOR = 'red'
SN_COLOR = 'white'

SN = 'snake'
OB = 'fruit'
SIZE = {SN: SN_SIZE, OB: OB_SIZE}

UP = 'Up'
DOWN = 'Down'
RIGHT = 'Right'
LEFT = 'Left'

DIRECTIONS = {UP: [0, -1], DOWN: [0, 1], RIGHT: [1, 0], LEFT: [-1, 0]}
AXES = {UP: 'Vertical', DOWN: 'Vertical', RIGHT: 'Horizontal', LEFT: 'Horizontal'}

REFRESH_TIME = 100


class Master(Canvas):
    def __init__(self, boss=None):
        super().__init__(boss)
        self.configure(width=WD, height=HT, bg=BG_COLOR)
        self.running = 0
        self.snake = None
        self.fruit = None
        self.direction = None
        self.current = None
        self.score = Scores(boss)

    def start(self):
        if self.running == 0:
            self.snake = Snake(self)
            self.fruit = Obstacle(self)
            self.direction = RIGHT
            self.current = Movement(self, RIGHT)
            self.current.begin()
            self.running = 1

    def clean(self):
        if self.running == 1:
            self.score.reset()
            self.current.stop()
            self.running = 0
            self.fruit.delete()
            for block in self.snake.blocks:
                block.delete()

    def redirect(self, event):
        if 1 == self.running and \
                event.keysym in AXES.keys() and\
                AXES[event.keysym] != AXES[self.direction]:
            self.current.flag = 0
            self.direction = event.keysym
            self.current = Movement(self, event.keysym)
            self.current.begin()


class Scores:
    def __init__(self, boss=None):
        self.counter = StringVar(boss, '0')
        self.maximum = StringVar(boss, '0')
        self.dict = {'score':0, 'counter':0}

    def increment(self):
        score = int(self.counter.get()) + 1
        maximum = max(score, int(self.maximum.get()))
        self.counter.set(str(score))
        self.maximum.set(str(maximum))
        self.dict['score'] = score
        self.dict['maximum'] = maximum
        self.declare_score()

    def reset(self):
        self.counter.set('0')
        self.dict['counter'] = self.counter

    def declare_score(self):
        addr = ('127.0.0.1', 8080)
        dict = self.dict

        message = "The score is {0}, the highest score is {1}".format(dict['score'], dict['maximum'])
        try:
            client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_sock.connect(addr)
            client_sock.send(message.encode('utf-8'))
            # print('LCH: json message sent to ', addr)
            client_sock.close()
            print('Success, the message is ', message)
        except socket.error as reason:
            print('Error, the reason is ', reason)


class Shape:
    def __init__(self, can, a, b, kind):
        self.can = can
        self.x, self.y = a, b
        self.kind = kind
        if kind == SN:
            self.ref = Canvas.create_rectangle(self.can,
                                               a - SN_SIZE, b - SN_SIZE,
                                               a + SN_SIZE, b + SN_SIZE,
                                               fill=SN_COLOR,
                                               width=2)
        elif kind == OB:
            self.ref = Canvas.create_oval(self.can,
                                          a - OB_SIZE, b - OB_SIZE,
                                          a + SN_SIZE, b + SN_SIZE,
                                          fill=OB_COLOR,
                                          width=2)

    def modify(self, a, b):
        self.x, self.y = a, b
        self.can.coords(self.ref,
                        a - SIZE[self.kind], b - SIZE[self.kind],
                        a + SIZE[self.kind], b + SIZE[self.kind])

    def delete(self):
        self.can.delete(self.ref)


class Obstacle(Shape):
    def __init__(self, can):
        self.can = can
        p = int(GRADUATION/2 - 1)
        n, m = randint(0, p), randint(0, p)
        a, b = PIXEL * (2 * n + 1), PIXEL * (2 * m + 1)
        while [a, b] in [[block.x, block.y] for block in self.can.snake.blocks]:
            n, m = randint(0, p), randint(0, p)
            a, b = PIXEL * (2 * n + 1), PIXEL * (2 * m + 1)
        super().__init__(can, a, b, OB)


class Block(Shape):
    def __init__(self, can, a, y):
        super().__init__(can, a, y, SN)


class Snake:
    def __init__(self, can):
        self.can = can
        a = PIXEL + 2 * int(GRADUATION/4) * PIXEL
        self.blocks = [Block(can, a, a), Block(can, a, a + STEP)]

    '''
    请在move函数中键入代码，实现贪吃蛇的移动、吃到果实、撞到身体失败、撞到边界失败的功能;
    '''
    def move(self, path_direction):
        a = (self.blocks[-1].x + STEP * path_direction[0])
        b = (self.blocks[-1].y + STEP * path_direction[1])

        fruit_x = self.can.fruit.x
        fruit_y = self.can.fruit.y

        if a > WD or a < 0 or b > HT or b < 0:
            self.can.clean()
        elif a == fruit_x and b == fruit_y:  # check if we find food
            self.can.score.increment()
            self.can.fruit.delete()
            self.blocks.append(Block(self.can, a, b))
            self.can.fruit = Obstacle(self.can)
        elif [a, b] in [[block.x, block.y] for block in self.blocks]:  # check if we hit a body part
            self.can.clean()
        else:
            # self.blocks[0].x = a
            # self.blocks[0].y = b
            self.blocks[0].modify(a, b)
            self.blocks = self.blocks[1:] + [self.blocks[0]]
            # self.blocks = self.blocks[1:]
            # self.blocks = self.blocks + [Block(self.can, a, b)]
            # self.blocks.append(Block(self.can, a, b))


class Movement:
    """object that enters the snake into a perpetual state of motion in a predefined direction"""
    def __init__(self, can, direction):
        self.flag = 1
        self.can = can
        self.direction = direction

    def begin(self):
        """start the perpetual motion"""
        if self.flag > 0:
            self.can.snake.move(DIRECTIONS[self.direction])
            self.can.after(REFRESH_TIME, self.begin)

    def stop(self):
        """stop the perpetual movement"""
        self.flag = 0


root = Tk()
root.title("Snake Game")
game = Master(root)
game.grid(column=1, row=0, rowspan=3)
root.bind("<Key>", game.redirect)
buttons = Frame(root, width=35, height=3*HT/5)
Button(buttons, text='Start', command=game.start).grid()
Button(buttons, text='Stop', command=game.clean).grid()
Button(buttons, text='Quit', command=root.destroy).grid()
buttons.grid(column=0, row=0)
scoreboard = Frame(root, width=35, height=2*HT/5)
Label(scoreboard, text='Game Score').grid()
Label(scoreboard, textvariable=game.score.counter).grid()
Label(scoreboard, text='High Score').grid()
Label(scoreboard, textvariable=game.score.maximum).grid()
scoreboard.grid(column=0, row=2)
root.mainloop()