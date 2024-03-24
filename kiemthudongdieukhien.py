class ABC:
    # def __init__(self, A, B, C):
    #     self.A = A
    #     self.B = B
    #     self.C = C
    
    def change(self, A, B, C):
        if (B > C):
            A = B
        else:
            A = C
        return A + B + C

 
class TestABC:
    def test_1(self):
        actual_output = ABC().change(1, 2, 3)
        expected_output = 8
        assert actual_output == expected_output
    def test_2(self):
        actual_output = ABC().change(1, 4, 3)
        expected_output = 11
        assert actual_output == expected_output