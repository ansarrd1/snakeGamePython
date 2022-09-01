from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highScore.txt") as file:
            self.highScore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}. High Score: {self.highScore}", align=ALIGNMENT, font=FONT)

    def resetScore(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open('highScore.txt', mode='w') as file:
                file.write(f"{self.highScore}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


