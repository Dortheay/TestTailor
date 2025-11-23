import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        int_0 = 0
        var_0 = lambda x: x % int_0 == int_0
        str_0 = '.'
        bool_0 = True
        iterator_0 = module_0.split_by(str_0, bool_0, separator=str_0)
        var_1 = list(iterator_0)
        str_1 = ' Split by: '
        iterator_1 = module_0.split_by(str_1)
        str_2 = ' Split by: '
        str_3 = ''
        var_2 = lambda x: x == str_3
        iterator_2 = module_0.split_by(str_2, criterion=var_2, separator=str_3)

if __name__ == "__main__":
    unittest.main()
