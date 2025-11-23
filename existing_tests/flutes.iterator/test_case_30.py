import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_31(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_22(self):
        try:
            int_0 = 3
            int_1 = 10
            var_0 = range(int_1)
            iterator_0 = module_0.drop(int_0, var_0)
            int_2 = 1952
            var_1 = range(int_1)
            iterator_1 = module_0.drop(int_2, var_1)
            var_2 = list(iterator_1)
            int_3 = 5
            var_3 = range(int_3)
            iterator_2 = module_0.drop(int_3, var_3)
            var_4 = list(iterator_2)
            var_5 = []
            iterator_3 = module_0.drop(int_0, var_5)
            var_6 = list(iterator_3)
            int_4 = -3
            var_7 = range(int_0)
            iterator_4 = module_0.drop(int_4, var_7)
            var_8 = list(iterator_4)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
