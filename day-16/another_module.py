# import another_module
# print(another_module.another_variable)
#
# from turtle import Turtle, Screen
#
# timmy = Turtle()
#
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# timmy.speed(1)
#
# my_screen = Screen()
# print(my_screen.canvheight)

from prettytable import PrettyTable

class CustomPrettyTable(PrettyTable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.vertical_char = "│"
        self.horizontal_char = "─"
        self.bottom_left_junction_char = "└"
        self.bottom_right_junction_char = "┘"
        self.top_left_junction_char = "┌"
        self.top_right_junction_char = "┐"
        self.left_junction_char = "├"
        self.right_junction_char = "┤"
        self.top_junction_char = "┬"
        self.bottom_junction_char = "┴"
        self.junction_char = "┼"
