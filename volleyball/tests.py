import unittest

from volleyball.players import MiddleBlocker, OutsideHitter, Setter
from volleyball.team import Team


class TestIsComplete(unittest.TestCase):
    def test_empty_team_false(self):
        wg_team = Team()
        self.assertFalse(wg_team.is_complete())
        
    def test_complete_team_true(self):
        wg_team = Team(
            {
                1: MiddleBlocker('oleg', 192, 96, 32), 
                2: OutsideHitter('dmitriy', 188, 96, 32), 
                3: Setter('sergey', 172, 96, 32), 
                4: MiddleBlocker('alex', 191, 96, 32), 
                5: OutsideHitter('igor', 194, 96, 32), 
                6: Setter('tanya', 167, 60, 25) 
            }                
        )
        self.assertTrue(wg_team.is_complete())
        
    def test_min_one_setter_false(self):
        wg_team = Team()
        wg_team[1] =  MiddleBlocker('oleg', 192, 96, 32)
        wg_team[2] =  OutsideHitter('dmitriy', 188, 96, 32)
        wg_team[3] =  OutsideHitter('sergey', 172, 96, 32)
        wg_team[4] =  MiddleBlocker('alex', 191, 96, 32)
        wg_team[5] =  OutsideHitter('igor', 194, 96, 32)
        wg_team[6] =  OutsideHitter('tanya', 167, 60, 25)
        wg_team[7] =  OutsideHitter('max', 191, 96, 32)
        self.assertFalse(wg_team.is_complete())
        
    def test_min_one_setter_true(self):
        wg_team = Team()
        wg_team[1] =  MiddleBlocker('oleg', 192, 96, 32)
        wg_team[2] =  OutsideHitter('dmitriy', 188, 96, 32)
        wg_team[3] =  Setter('sergey', 172, 96, 32)
        wg_team[4] =  MiddleBlocker('alex', 191, 96, 32)
        wg_team[5] =  OutsideHitter('igor', 194, 96, 32)
        wg_team[6] =  Setter('tanya', 167, 60, 25)
        wg_team[7] =  OutsideHitter('max', 191, 96, 32)
        wg_team[8] =  Setter('anya', 160, 50, 21)
        self.assertTrue(wg_team.is_complete())
        
    def test_count_hitter_true(self):
        wg_team = Team(
            {
                1: MiddleBlocker('oleg', 192, 96, 32), 
                2: OutsideHitter('dmitriy', 188, 96, 32), 
                3: Setter('sergey', 172, 96, 32), 
                4: MiddleBlocker('alex', 191, 96, 32), 
                5: OutsideHitter('igor', 194, 96, 32), 
                6: Setter('tanya', 167, 60, 25), 
                7: OutsideHitter('max', 191, 96, 32)
            }                
        )
        self.assertTrue(wg_team.is_complete())
        
    def test_count_hitter_false(self):
        wg_team = Team(
            {
                1: MiddleBlocker('oleg', 192, 96, 32), 
                2: Setter('dmitriy', 188, 96, 32), 
                3: Setter('sergey', 172, 96, 32), 
                4: MiddleBlocker('alex', 191, 96, 32), 
                5: OutsideHitter('igor', 194, 96, 32), 
                6: Setter('tanya', 167, 60, 25), 
                7: Setter('anya', 160, 50, 21)
            }                
        )
        self.assertFalse(wg_team.is_complete())
        
    def test_count_pleyrs_false(self):
        wg_team = Team(
            {
                1: MiddleBlocker('oleg', 192, 96, 32), 
                2: OutsideHitter('dmitriy', 188, 96, 32), 
                3: Setter('sergey', 172, 96, 32), 
                4: MiddleBlocker('alex', 191, 96, 32), 
                5: OutsideHitter('igor', 194, 96, 32)
            }                
        )
        self.assertFalse(wg_team.is_complete())
        
    def test_position_players_true(self):
        wg_team = Team()
        wg_team[1] =  MiddleBlocker('oleg', 192, 96, 32)
        wg_team[2] =  Setter('tanya', 167, 60, 25)
        wg_team[3] =  OutsideHitter('jora', 188, 96, 32)
        wg_team[4] =  MiddleBlocker('alexey', 191, 96, 32)
        wg_team[5] =  Setter('sergey', 172, 96, 32)        
        wg_team[6] =  OutsideHitter('alex', 194, 96, 32)        
        self.assertTrue(wg_team.initial_positions())
    
    def test_position_players_false(self):
        wg_team = Team()
        wg_team[3] =  MiddleBlocker('oleg', 192, 96, 32)
        wg_team[1] =  OutsideHitter('jora', 188, 96, 32)
        wg_team[5] =  Setter('sergey', 172, 96, 32)
        wg_team[4] =  MiddleBlocker('alexey', 191, 96, 32)
        wg_team[6] =  OutsideHitter('alex', 194, 96, 32)
        wg_team[2] =  Setter('tanya', 167, 60, 25)
        self.assertFalse(wg_team.initial_positions())
        
    def test_count_position_players_false(self):
        wg_team = Team()
        wg_team[3] =  MiddleBlocker('oleg', 192, 96, 32)
        wg_team[5] =  Setter('sergey', 172, 96, 32)
        wg_team[4] =  MiddleBlocker('alexey', 191, 96, 32)
        wg_team[6] =  OutsideHitter('alex', 194, 96, 32)
        wg_team[2] =  Setter('tanya', 167, 60, 25)
        self.assertFalse(wg_team.initial_positions())
        
    def test_count_position_players_true(self):
        wg_team = Team()
        wg_team[3] =  MiddleBlocker('oleg', 192, 96, 32)
        wg_team[1] =  OutsideHitter('jora', 188, 96, 32)
        wg_team[5] =  Setter('anya', 160, 50, 21)
        wg_team[4] =  MiddleBlocker('alexey', 191, 96, 32)
        wg_team[6] =  OutsideHitter('alex', 194, 96, 32)
        wg_team[2] =  Setter('tanya', 167, 60, 25)
        self.assertTrue(wg_team.initial_positions())
        
        
        
        


#class TestInitialPosition(TestCase):
            
if __name__ == '__main__':
    unittest.main()
