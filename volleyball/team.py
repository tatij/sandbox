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
        '''
        return initial positions of players as a dict where
        positions on the court are keys and players are values.
        For example:
            {
                1: <MiddleBlocker object>,
                2: <Setter object>,
                3: <OutsideHitter object>,
                4: <MiddleBlocker object>,
                5: <Setter object>,
                6: <OutsideHitter object>
            }
        '''
        result = {}
        # TODO: rework following code
        for num, player in self.items(): 
            if isinstance(player, MiddleBlocker):
                result[3] = player
                result[6] = player
            if isinstance(player, Setter):
                result[1] = player
                result[4] = player
            if isinstance(player, OutsideHitter):
                result[2] = player
                result[5] = player
        return(result)         
        
                                   
class Set:
    pass


class Game:
    pass
