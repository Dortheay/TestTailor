import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        int_0 = 10
        var_0 = range(int_0)
        iterator_0 = module_0.split_by(var_0, criterion=int_0)
        str_0 = ' Split by: '
        str_1 = '.'
        iterator_1 = module_0.split_by(str_0, separator=str_1)
        var_1 = list(iterator_1)
        str_2 = ' Split by: '
        iterator_2 = module_0.split_by(str_2)

if __name__ == "__main__":
    unittest.main()
