class Item:
    def __init__(self, position, color, name):
        self.position = position
        self.color = color
        self.name = name

    def __str__(self):
        return f"Item {self.name} of color {self.color} at {self.position}"