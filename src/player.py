# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, location):
        self.location = location

    def try_direction(self, command):
        attritube = command + '_to'

        # see if the current room has the attribute
        if hasattr(self.location, attritube):
            # use 'getattr' to actually move to the room
            self.location = getattr(self.location, attribute)
        else:
            print("You can't go that way!\n")
