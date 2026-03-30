class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"Flower Name: {self.name}, Color: {self.color}"

my_flower = Flower("Rose", "Red")

print(my_flower)