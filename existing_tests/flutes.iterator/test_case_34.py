import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_35(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_26(self):
        try:
            int_0 = 5
            int_1 = 10
            var_0 = range(int_1)
            iterator_0 = module_0.take(int_0, var_0)
            var_1 = list(iterator_0)
            int_2 = 15
            var_2 = range(int_1)
            var_3 = None
            iterator_1 = module_0.take(int_2, var_3)
            var_4 = list(iterator_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
