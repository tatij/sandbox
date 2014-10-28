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
        
if __name__ == '__main__':
    unittest.main()
