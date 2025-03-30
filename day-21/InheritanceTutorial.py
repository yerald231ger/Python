class Animal:
    sound: str
    def __init__(self, name):
        self.name = name

    def breathe(self):
        return "Some sound"

class Fish:

    def swim(self):
        return "Gulp gulp"


memo = Fish()
