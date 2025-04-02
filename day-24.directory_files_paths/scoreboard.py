from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

def get_high_score():
    with open("data.txt", "r") as file:
        return int(file.read())

def update_high_score(score):
    with open("data.txt", "w") as file:
        file.write(str(score))


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = get_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            update_high_score(self.score)
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
