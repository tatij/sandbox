from volleyball.players import MiddleBlocker, OutsideHitter, Setter


class Team(dict):
    
    def is_complete(self): 
        count_MiddleBlocker = 0
        count_OutsideHitter = 0
        count_Setter = 0
        count_players = 0
        for num, player in self.items():
            count_players = count_players + 1
            if isinstance(player, MiddleBlocker):
                count_MiddleBlocker = count_MiddleBlocker + 1
            elif isinstance(player, OutsideHitter):
                count_OutsideHitter = count_OutsideHitter + 1
            elif isinstance(player, Setter):
                count_Setter = count_Setter + 1
        if count_MiddleBlocker < 2 or count_OutsideHitter < 2 or count_Setter < 2 or count_players < 6:
            return False
        else:
            return True
        print(count_MiddleBlocker)
        print(count_OutsideHitter)
        print(count_Setter)
    
    def initial_positions(self):
        pass
    
    
class Set:
    pass


class Game:
    pass