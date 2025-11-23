import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_30(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_21(self):
        try:
            int_0 = 5
            int_1 = 10
            var_0 = range(int_1)
            iterator_0 = module_0.take(int_0, var_0)
            var_1 = list(iterator_0)
            int_2 = 15
            var_2 = range(int_1)
            iterator_1 = module_0.take(int_2, var_2)
            var_3 = list(iterator_1)
            int_3 = 0
            var_4 = range(int_1)
            iterator_2 = module_0.take(int_3, var_4)
            var_5 = list(iterator_2)
            var_6 = list(iterator_1)
            int_4 = -1
            iterator_3 = module_0.take(int_4, int_3)
            var_7 = list(iterator_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
