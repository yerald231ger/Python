class Animal:

    def __init__(self, name):
        self.name = name

    def breathe(self):
        return "Inhale, exhale"


class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def breathe(self):
        super().breathe()
        return "Breathe through the gills"

    def swim(self):
        return "Swimming in the water"


animal = Animal("Rex")
memo = Fish("Nemo")
print(memo.swim())
print(memo.breathe())
print(memo.name)
