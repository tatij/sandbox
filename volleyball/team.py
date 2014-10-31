from volleyball.players import MiddleBlocker, OutsideHitter, Setter


class Team(dict):
    
    def is_complete(self): 
        count_MiddleBlocker = 0
        count_OutsideHitter = 0
        count_Setter = 0
        count_players = 0
        for player in self.values():
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
    
    def initial_positions(self):
        result = 0
        for num, player in self.items(): 
            if isinstance(player, MiddleBlocker):
                if num == 1 or num == 4:
                    result = result + 1
                    print("1_4")
            elif isinstance(player, Setter):
                if num == 2 or num == 5:
                    result = result + 1
                    print("2_5")
            elif isinstance(player, OutsideHitter):
                if num == 3 or num == 6:
                    result = result + 1
                    print("3_6")
        if result == 3:
            return True
        else:
            return False    
        
                                   
class Set:
    pass


class Game:
    pass