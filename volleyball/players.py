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
    def move_front(self):
        pass
    def meet_ball(self):
        pass
    #def move_back(self):
        #pass
class Hitter(Player):
    def block(self):
        pass
    def meet_block(self):
        pass
    def beat(self, position):
        if position == 2:
            self.beat_week()
        elif position == 3:
            self.beat_middle()
        elif position == 4:
            self.beat_out()
class Setter(Player):
    def give_pass(self, position):
        self.beat(position)
class OutsideHitter(Hitter):
    def beat_out(self):
        while not self.meet_ball():
            self.move_front()
class WeeksideHitter(Hitter):
    def beat_week(self):
        while not self.meet_ball():
            self.move_front()
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
    def beat_middle(self):
        while not self.meet_ball():
            self.move_front()