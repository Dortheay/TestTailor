import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_29(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        try:
            int_0 = 3
            int_1 = 10
            var_0 = range(int_1)
            iterator_0 = module_0.chunk(int_0, var_0)
            var_1 = list(iterator_0)
            int_2 = 5
            int_3 = 1
            int_4 = 2
            int_5 = [int_3, int_4, int_0]
            iterator_1 = module_0.chunk(int_2, int_5)
            var_2 = list(iterator_1)
            int_6 = [int_3, int_4, int_0]
            iterator_2 = module_0.chunk(int_3, int_6)
            var_3 = list(iterator_2)
            var_4 = []
            iterator_3 = module_0.chunk(int_0, var_4)
            var_5 = list(iterator_3)
            int_7 = [int_3, int_4, int_0]
            iterator_4 = module_0.chunk(int_0, int_7)
            var_6 = list(iterator_4)
            int_8 = 1
            int_9 = 3
            int_10 = [int_8, int_8, int_9]
            iterator_5 = module_0.chunk(int_4, int_10)
            var_7 = list(iterator_5)
            int_11 = -1
            int_12 = 1
            int_13 = 2
            int_14 = -26
            int_15 = [int_12, int_13, int_14]
            iterator_6 = module_0.chunk(int_11, int_15)
            var_8 = list(iterator_6)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
