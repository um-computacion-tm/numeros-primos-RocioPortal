import unittest

def is_primo(value):
    if value < 1:  
        return False
    for i in range(2, value):  
        if value % i == 0:  
            return False
    return True  

class TestPrimos(unittest.TestCase):
    def test_1(self):
        result = is_primo(1)
        self.assertEqual(result, True)
    
    def test_2(self):
        result = is_primo(2)
        self.assertEqual(result, True)

    def test_3(self):
        result = is_primo(3)
        self.assertEqual(result, True)

    def test_4(self):
        result = is_primo(4)
        self.assertEqual(result, False)

    def test_5(self):
        result = is_primo(5)
        self.assertEqual(result, True)

    def test_6(self):
        result = is_primo(6)
        self.assertEqual(result, False)

    def test_30(self):
        result = is_primo(30)
        self.assertEqual(result, False)

    def test_1049(self):
        result = is_primo(1049)
        self.assertEqual(result, True)
    
    def test_negativo(self):
        result = is_primo(-4)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()