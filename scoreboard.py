from turtle import Turtle

ALIGNMENT = "center"
POSITION_X = 0
POSITION_Y = 280
STARTING_SCORE = 0
TEXT_COLOR = "white"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        with open("high_score.txt") as file:
            content = file.read()
            self.high_score = int(content)
        self.goto(POSITION_X, POSITION_Y)
        self.color(TEXT_COLOR)
        self.hideturtle()
        self.score = STARTING_SCORE
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score} High score: {self.high_score}", False, ALIGNMENT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))
        self.clear_score()

    def clear_score(self):
        self.clear()
        self.score = STARTING_SCORE
        self.write_score()
