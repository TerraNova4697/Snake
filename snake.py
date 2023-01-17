from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_block(position)

    def move(self):
        for block_index in range(len(self.blocks) - 1, -1, -1):
            if block_index == 0:
                self.blocks[block_index].forward(MOVE_DISTANCE)
            else:
                next_block_pos = self.blocks[block_index - 1].pos()
                self.blocks[block_index].goto(next_block_pos)

    def extend(self):
        self.add_block(self.blocks[-1].position())

    def reset(self):
        for block in self.blocks:
            block.goto(1000, 1000)
        self.blocks.clear()
        self.create_snake()
        self.head = self.blocks[0]

    def add_block(self, position):
        block = Turtle("square")
        block.color("white")
        block.penup()
        block.goto(position)
        self.blocks.append(block)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
