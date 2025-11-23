import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_27(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        try:
            float_0 = -2265.1
            bool_0 = True
            iterator_0 = module_0.split_by(float_0, bool_0)
            list_0 = []
            lazy_list_0 = module_0.LazyList(list_0)
            list_1 = [list_0, bool_0]
            var_0 = module_0.scanr(iterator_0, lazy_list_0, *list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
