import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_32(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_23(self):
        try:
            int_0 = 0
            var_0 = lambda x: x >= int_0
            var_1 = range(int_0)
            iterator_0 = module_0.drop_until(var_0, var_1)
            var_2 = list(iterator_0)
            var_3 = lambda x: x > int_0
            var_4 = []
            iterator_1 = module_0.drop_until(var_3, var_4)
            var_5 = list(iterator_1)
            var_6 = lambda x: x > int_0
            int_1 = [int_0]
            iterator_2 = module_0.drop_until(var_6, int_1)
            var_7 = list(iterator_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
