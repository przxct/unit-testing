class Document:
    def __init__(self, typeDocument, time):
        self.typeDocument = typeDocument
        self.time = time
 
    def action(self):
        # typeDoc = 1, hop dong
        # typeDoc = 2, bao cao nhan vien
        # typeDoc = 3, so sach
        
        if self.typeDocument == 1 or self.typeDocument == 3:
            if self.time >= 2000:
                return "giay to quan trong"
            else:
                return "giay to binh thuong"
        else:
            if self.time >= 2010:
                return "giay to binh thuong"
            else:
                return "vut bo"

 
class TestSchoolarShip:
    def test_1(self):
        document = Document(1, 2020)
        expected_output = "giay to quan trong"
        actual_output = document.action()
        assert actual_output == expected_output

    def test_2(self):
        document = Document(1, 2009)
        expected_output = "giay to quan trong"
        actual_output = document.action()
        assert actual_output == expected_output
    
    def test_3(self):
        document = Document(1, 1890)
        expected_output = "giay to binh thuong"
        actual_output = document.action()
        assert actual_output == expected_output
    
    def test_4(self):
        document = Document(2, 2024)
        expected_output = "giay to binh thuong"
        actual_output = document.action()
        assert actual_output == expected_output

    def test_5(self):
        document = Document(2, 2008)
        expected_output = "vut bo"
        actual_output = document.action()
        assert actual_output == expected_output
    
    def test_6(self):
        document = Document(2, 1990)
        expected_output = "vut bo"
        actual_output = document.action()
        assert actual_output == expected_output
    
    def test_7(self):
        document = Document(3, 2010)
        expected_output = "giay to quan trong"
        actual_output = document.action()
        assert actual_output == expected_output
    
    def test_8(self):
        document = Document(3, 2003)
        expected_output = "giay to quan trong"
        actual_output = document.action()
        assert actual_output == expected_output
    
    def test_9(self):
        document = Document(3, 1980)
        expected_output = "giay to binh thuong"
        actual_output = document.action()
        assert actual_output == expected_output