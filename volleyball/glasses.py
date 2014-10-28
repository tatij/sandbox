class TestGlasses(unittest.TestCase):
    def test_form_false(self):
        form = Form_glasses()
        self.assertFalse(form.is_form())
        
    def test_form_true(self):
        form = Form_glasses(
            {
                1: Round(), 
                2: Square(), 
                3: Oval(), 
                4: Rectangular()
            }                
        )
        self.assertTrue(form.is_form())
