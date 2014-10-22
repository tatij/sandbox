class Player:
    def __init__(self, name, height, weight, age):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
    def move_right(self):
	    pass
	def move_left(self):
	    pass
class Hitter(Player):
    def block(self):
	    pass
class Setter(Player):
    pass
class OutsideHitter(Hitter):
    pass
class WeeksideHitter(Hitter):
    pass
class MiddleBlocker(Hitter):
    def block(self, position):
        if position == 2:
            while not self.meet_block():
                self.move_right()
                super().block()
        elif position == 3:
            super().block()
        elif position == 4:
            while not self.meet_block():
                self.move_left()
                super().block()