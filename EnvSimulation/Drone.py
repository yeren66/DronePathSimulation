from Environment import Environment
from Item import Item

class Drone:
    def __init__(self, env:Environment, number=0, position=(0, 0, 0)):
        self.env = env
        self.number = number
        self.position = position
        self.carrying_item = None
    
    def takeOff(self, height):
        self.position = (self.position[0], self.position[1], height)
        print(f"Drone {self.number} took off to height {height}")
    
    def moveCtrl(self, direction, distance):
        x, y, z = self.position
        if direction == 0:  # x
            x += distance
        elif direction == 1:  # y
            y += distance
        elif direction == 2:  # z
            z += distance
        elif direction == 3:  # -x
            x -= distance
        elif direction == 4:  # -y
            y -= distance
        elif direction == 5:  # -z
            z -= distance
        self.position = (x, y, z)
        print(f"Drone {self.number} moved to {self.position}")
    
    def flyCtrl(self, height):
        x, y, _ = self.position
        self.position = (x, y, height)
        print(f"Drone {self.number} landed at height {height}")
    
    def position_detect(self):
        print(f"Drone {self.number} current position: {self.position}")
        return self.position
    
    def pickItem(self):
        if self.carrying_item:
            return False
        ret = self.env.WhetherPick(self.position)
        if ret == None:
            return False
        else:
            self.carrying_item = ret
        return True
    
    def placeItem(self):
        if self.carrying_item:
            self.env.placeItem(self.position, self.carrying_item)
            self.carrying_item = None
            print(f"Drone {self.number} placed down the item")
            return True
        return False
    
    def detectColor(self):
        return self.carrying_item.color
    
    

def takeOff(drone, height):
    drone.takeOff(height)


def moveCtrl(drone, direction, distance):
    drone.moveCtrl(direction, distance)


def flyCtrl(drone, height):
    drone.flyCtrl(height)


def position_detect(drone):
    return drone.position_detect()


def pickItem(drone):
    return drone.pickItem()


def placeItem(drone):
    return drone.placeItem()


def detectColor(drone):
    return drone.detectColor()
    