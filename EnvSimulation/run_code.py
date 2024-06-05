from Drone import Drone
from Drone import takeOff, moveCtrl, flyCtrl, position_detect, pickItem, placeItem, detectColor
from Environment import Environment
from Item import Item


def sort_items_by_color(drone_number: Drone, pickup_location: tuple, item_ids: list, color_areas: dict) -> str:
    """
    Navigates a drone to pick up items, detect their colors, and place them in designated areas based on the color.

    Parameters:
        drone_number (int): Identifier for the drone.
        pickup_location (tuple): Coordinates (x, y, z) where items are picked up.
        item_ids (list): List of item identifiers available for pickup.
        color_areas (dict): Dictionary mapping colors to area coordinates for item placement.

    Returns:
        str: A message indicating the success or failure of the operations.

    Errors Handled:
        - Incorrect item_id leading to failed pickup attempts.
        - Unrecognized colors resulting in no corresponding placement area.
        - Drone movement errors such as unable to reach locations due to obstacles or range limitations.
    """
    # Command the drone to take off and move to the pickup location
    takeOff(drone_number, pickup_location[2])
    moveCtrl(drone_number, 0, pickup_location[0])
    moveCtrl(drone_number, 1, pickup_location[1])

    # Start picking up items
    for item_id in item_ids:
        # Detect current position
        current_position = position_detect(drone_number)
        if current_position != pickup_location:
            moveCtrl(drone_number, 0, pickup_location[0] - current_position[0])
            moveCtrl(drone_number, 1, pickup_location[1] - current_position[1])

        # Attempt to pick up the item
        if not pickItem(drone_number):
            return f"Failed to pick up item {item_id}."
        
        # Detect the color of the item
        color = detectColor(drone_number)
        if color not in color_areas:
            placeItem(drone_number)  # Place item back if no corresponding area
            return f"No designated area for color {color}."
        
        # Navigate to the designated area for the detected color
        placement_location = color_areas[color]
        moveCtrl(drone_number, 0, placement_location[0] - pickup_location[0])
        moveCtrl(drone_number, 1, placement_location[1] - pickup_location[1])
        
        # Place the item down
        if not placeItem(drone_number):
            return f"Failed to place item {item_id} in the designated area."

        # Return to pickup location for next item
        moveCtrl(drone_number, 0, pickup_location[0] - placement_location[0])
        moveCtrl(drone_number, 1, pickup_location[1] - placement_location[1])

    # Land the drone after operations
    flyCtrl(drone_number, 0)

    return "All items have been successfully sorted and placed."

if __name__ == "__main__":
    # scenario 1
    pickup = (10, 10, 0)
    items = [Item((10, 10, 0), "red", "item1"), Item((10, 10, 0), "blue", "item2"), Item((10, 10, 0), "yellow", "item3")]
    color_area = {"red": (100, 10, 0), "blue": (10, 100, 0), "yellow": (50, 50, 0)}
    env = Environment(pickup, items, color_area)
    drone = Drone(env, 0, (0, 0, 0))
    color_areas = {"red": (100, 10, 0), "blue": (10, 100, 0), "yellow": (50, 50, 0)}
    result = sort_items_by_color(drone, (10, 10, 0), ["item1", "item2", "item3"], color_areas)
    print(result)
    print("Judge:")
    env.judge()