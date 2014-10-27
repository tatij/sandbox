class Player:
    '''
    Base class for any volleyball playyer
    '''
    def __init__(self, name, height, weight, age):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
    def move_right(self):
        '''
        move player one step right
        '''
        pass
    def move_left(self):
        '''
        move player one step left
        '''
        pass   
    def move_front(self):
        pass
    def meet_ball(self):
        pass
    #def move_back(self):
        #pass
class Hitter(Player):
    '''
    Any Hitter
    '''
    def block(self, position):
        '''
        block hitter 
        '''
        pass
    def meet_block(self):
        '''
        check whether player have met teammate which are going to block hit
        '''
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
    '''
    Teams outside hitters are usually the primary attackers on the team. 
    These hitters attack balls that are set to the left side of the court. 
    Outside hitters may also be referred to as outside blockers.
    '''
    def beat_out(self):
        while not self.meet_ball():
            self.move_front() 
class WeeksideHitter(Hitter):
    '''
    Team`s weak side hitters hit from the right side of the court and are 
    usually not the primary attackers on the team. 
    Weakside hitters may also be referred to as weakside blockers.
    '''
    def beat_week(self):
        while not self.meet_ball():
            self.move_front()
class MiddleBlocker(Hitter):
    '''
    On defense, the Middle Blocker position is the player at the net in the 
    middle of the court between the two outside blockers. The middle blocker 
    strives to be involved in blocking the opponent's hitters wherever 
    they may be on the court. On offense, the middle blocker will usually 
    hit quick sets or serve as a decoy to confuse the opponent's 
    blockers if the pass is good enough.
    '''
    def block(self, position):
        '''
        block hitter 
        '''
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
