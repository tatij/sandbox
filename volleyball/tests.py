from unittest import TestCase
class TestIsComplete(TestCase):
    def test_empty_team_false(self):
        wg_team = Team()
        self.assertFalse(wg_team.is_complete())
        
    def test_complete_team_true(self):
        wg_team = Team(
            {
                1: MiddleBlock(), 
                2: OutsideHitter(), 
                3: Setter(), 
                4: MiddleBlock(), 
                5: OutsideHitter(), 
                6: Setter() 
            }                
        )
        self.assertTrue(wg_team.is_complete())
        
if __name__ == '__main__':
    unittest.main()