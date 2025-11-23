import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        int_0 = -17
        var_0 = range(int_0)
        lazy_list_0 = module_0.LazyList(var_0)
        var_1 = list(lazy_list_0)
        var_2 = len(lazy_list_0)
        var_3 = iter(lazy_list_0)
        var_4 = list(lazy_list_0)
        var_5 = len(lazy_list_0)

if __name__ == "__main__":
    unittest.main()
