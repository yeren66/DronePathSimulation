from Item import Item


class Environment:
    def __init__(self, pickup: tuple, items: list[Item], color_area: dict):
        self.pickup = pickup
        self.items = items
        self.color_area = color_area

    def WhetherPick(self, drone_position):
        for item in self.items:
            if item.position == drone_position:
                return item
        return None
    
    def placeItem(self, position, item):
        item.position = position
    
    def judge(self):
        fail = False
        for item in self.items:
            if item.position != self.color_area[item.color]:
                print(f"Item {item.name} of color {item.color} is not in the correct area.")
                fail = True
            else:
                print(f"Item {item.name} of color {item.color} is in the correct area.")
        return not fail