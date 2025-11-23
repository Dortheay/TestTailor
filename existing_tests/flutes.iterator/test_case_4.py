import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = '.'
        iterator_0 = module_0.split_by(str_0, separator=str_0)
        var_0 = list(iterator_0)
        iterator_1 = module_0.split_by(str_0)

if __name__ == "__main__":
    unittest.main()
