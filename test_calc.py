import unittest
import calc


# to run test python -m unittest test_calc.py
# if no [if __name__ == "__main__":]
class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10,5), 15)
        # test edge cases
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)


    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5), 5)
        # test edge cases
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)


    def test_multiply(self):
        self.assertEqual(calc.multiply(10,5), 50)
        # test edge cases
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)


    def test_divide(self):
        self.assertEqual(calc.divide(10,5), 2)
        # test edge cases
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)

        # to test the RaiseError
        self.assertRaises(ValueError, calc.divide, 10, 0)

# since this is here you can run test just will
# python test_calc.py
if __name__ == "__main__":
    unittest.main()
