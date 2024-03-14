class SchoolarShip:
    def __init__(self, toan, van, anh, chuyen):
        self.toan = toan
        self.van = van
        self.anh = anh
        self.chuyen = chuyen
 
    def get_sum_points(self):
        return self.toan + self.van + self.anh + self.chuyen
    
    def type_schoolar_ship(self):
        sum_points = self.toan + self.van + self.anh + self.chuyen
        if sum_points >= 30 and sum_points <= 50:
            return "10.000.000"
        if (sum_points >= 20 and sum_points < 30):
	        return "5.000.000"
        if (sum_points >= 15 and sum_points < 20):
	        return "3.000.000"
        if (sum_points >= 0 and sum_points < 15):
	        return "0"
        return "error"

 
class TestSchoolarShip:
    def test_1(self):
        schoolarShip = SchoolarShip(5, 5, 5, 10)
        expected_output = "5.000.000"
        actual_output = schoolarShip.type_schoolar_ship()
        assert actual_output == expected_output
    
    def test_2(self):
        schoolarShip = SchoolarShip(5, 5, 5, 0)
        expected_output = "3.000.000"
        actual_output = schoolarShip.type_schoolar_ship()
        assert actual_output == expected_output
    
    def test_3(self):
        schoolarShip = SchoolarShip(5, 5, 5, 1)
        expected_output = "3.000.000"
        actual_output = schoolarShip.type_schoolar_ship()
        assert actual_output == expected_output
    
    def test_4(self):
        schoolarShip = SchoolarShip(5, 5, 5, 19)
        expected_output = "10.000.000"
        actual_output = schoolarShip.type_schoolar_ship()
        assert actual_output == expected_output
    
    def test_5(self):
        schoolarShip = SchoolarShip(5, 5, 5, 20)
        expected_output = "10.000.000"
        actual_output = schoolarShip.type_schoolar_ship()
        assert actual_output == expected_output
    
    def test_6(self):
        schoolarShip = SchoolarShip(5, 5, 0, 10)
        expected_output = "5.000.000"
        actual_output = schoolarShip.type_schoolar_ship()
        assert actual_output == expected_output
    
    def test_7(self):
        schoolarShip = SchoolarShip(5, 5, 1, 10)
        expected_output = "5.000.000"
        actual_output = schoolarShip.type_schoolar_ship()
        assert actual_output == expected_output
    
    def test_8(self):
        schoolarShip = SchoolarShip(5, 5, 9, 10)
        expected_output = "5.000.000"
        actual_output = schoolarShip.type_schoolar_ship()
        assert actual_output == expected_output
    
    def test_9(self):
        schoolarShip = SchoolarShip(5, 5, 10, 10)
        expected_output = "10.000.000"
        actual_output = schoolarShip.type_schoolar_ship()
        assert actual_output == expected_output
    
    def test_10(self):
        schoolarShip = SchoolarShip(5, 0, 5, 10)
        expected_output = "5.000.000"
        actual_output = schoolarShip.type_schoolar_ship()
        assert actual_output == expected_output
    
    def test_11(self):
        schoolarShip = SchoolarShip(5, 1, 5, 10)
        expected_output = "5.000.000"
        actual_output = schoolarShip.type_schoolar_ship()
        assert actual_output == expected_output
    
    def test_12(self):
        schoolarShip = SchoolarShip(5, 9, 5, 10)
        expected_output = "5.000.000"
        actual_output = schoolarShip.type_schoolar_ship()
        assert actual_output == expected_output
    
    def test_13(self):
        schoolarShip = SchoolarShip(5, 10, 5, 10)
        expected_output = "10.000.000"
        actual_output = schoolarShip.type_schoolar_ship()
        assert actual_output == expected_output
    
    def test_14(self):
        schoolarShip = SchoolarShip(0, 5, 5, 10)
        expected_output = "5.000.000"
        actual_output = schoolarShip.type_schoolar_ship()
        assert actual_output == expected_output
    
    def test_15(self):
        schoolarShip = SchoolarShip(1, 5, 5, 10)
        expected_output = "5.000.000"
        actual_output = schoolarShip.type_schoolar_ship()
        assert actual_output == expected_output
    
    def test_16(self):
        schoolarShip = SchoolarShip(9, 5, 5, 10)
        expected_output = "5.000.000"
        actual_output = schoolarShip.type_schoolar_ship()
        assert actual_output == expected_output
    
    def test_17(self):
        schoolarShip = SchoolarShip(10, 5, 5, 10)
        expected_output = "10.000.000"
        actual_output = schoolarShip.type_schoolar_ship()
        assert actual_output == expected_output