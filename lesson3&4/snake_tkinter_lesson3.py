from tkinter import *
from random import randint
# new lines here
import socket
# new lines end

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

        # new lines here
        self.dict = {'score': 0, 'maximum': 0}
        # new lines end

    def increment(self):
        score = int(self.counter.get()) + 1
        maximum = max(score, int(self.maximum.get()))
        self.counter.set(str(score))
        self.maximum.set(str(maximum))
        # new lines here
        self.declare_score()
        self.dict['score'] = score
        self.dict['maximum'] = maximum
        # new lines end

    def reset(self):
        self.counter.set('0')

        # new lines here
    def declare_score(self):
        addr = ('127.0.0.1', 8080) # 服务器端的ip地址和端口号
        dict = self.dict
        # new lines end
        
        '''
        小练习：
            addr是Server的IP地址和端口号，请根据需要进行改写
            dict是一个字典，有两个key，分别是‘score’和‘maximum’，代表了现在的得分和最高分
            
            要求：
                1）创建一个字符串message，使用format函数对字符串进行操作，将贪食蛇的得分和最高分包含入message中
                2）使用socket将message发送至Server，注意对message进行编码（encode('utf-8')）
                3）使用try-except对socket的远程通讯进行把控，如果执行失败打印'Error, the message is not sent！'
                4）请在 Your code here 处编写你的代码段
        
        '''

        ''' Your code here'''
        
        
        
        ''' Your code here'''


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
    请在move函数中键入代码,使用if, elif, else实现贪吃蛇吃到果实、撞到身体失败、撞到边界失败的功能;
    变量a, b分别为贪吃蛇下一步蛇头位置的x, y坐标;
    fruit_x, fruit_y分别为果实的x, y坐标, 如果贪吃蛇的蛇头坐标与果实坐标重合, 则判定贪吃蛇吃到了果实, 贪吃蛇在蛇头位置增加长度;
    WD, HT为地图的宽度和长度, 例如贪吃蛇的蛇头x坐标大于WD或小于0, 则判定贪吃蛇撞到了边界, 对蛇头y坐标亦然;
    贪吃蛇的身体储存在self.blocks中, [[block.x, block.y] for block in self.blocks]是贪吃蛇身体的坐标信息列表, 如果蛇头坐标与身体坐标信息列表的任意一个重合, 则判定贪吃蛇撞到了身体, 请使用in判定;
    若贪吃蛇在正常移动, 它的身体长度应保持不变, 请运用列表的操作将贪吃蛇身体列表self.blocks的第一个元素（蛇尾）提取出来并将其改造成为下一步的蛇头, 改变贪吃蛇尾巴位置使用self.blocks[0].modify(a, b);
    
    涉及知识点： 函数; 条件表达式; if语句; 列表操作; 
    
    注意：
    贪吃蛇的身体由Block组成, 调用Block(self.can, x坐标, y坐标)可以为贪吃蛇生成新的身体部分;
    贪吃蛇的身体保存为self.blocks, self.blocks[0]为蛇尾, self.blocks[-1]为蛇头;
    请将\'''Your code here\'''改为你的代码
    
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
            self.blocks[0].modify(a, b)
            self.blocks = self.blocks[1:] + [self.blocks[0]]


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
