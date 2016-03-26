import random

class Room:
    def __init__(self, exits, inspect_text, items):
        self.exits = exits
        self.inspect_text = inspect_text
        self.items = items

    def inspect(self):
        return "Looking around, you see " + self.inspect_text

class RoomFactory:
    def __init__(self):
        return

    def make_room(self):
        item_list = ["fork", "banana", "table", "rock", "sword", "mug", "ghost", "battle hamster"]
        items = []
        for i in range(0, random.randint(1, 3)):
            items.append(item_list[random.randint(0, 7)])

        exits = ["west", "east", "down"]
        inspect_text = "the room "
        if random.random() > 0.5:
            inspect_text += "is nice"
            if random.random() > 0.5:
                inspect_text += " although it smells strange. "
            else:
                inspect_text += ". "
        else:
            inspect_text += "is not very nice. "

        if items:
            for item in items:
                inspect_text += "There is a "+ item +" here. "

        return Room(exits, inspect_text, items)

