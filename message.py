import turtle as tt
import settings
#  # Creating this class, so I can write messages where I want


class Message(tt.Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.font = settings.FONT

    def write_name(self, arg, position):
        self.goto(position)
        self.write(arg=arg, move=False, align="center", font=self.font)