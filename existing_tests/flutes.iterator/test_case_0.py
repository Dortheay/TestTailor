import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = '$:]jL8\x0cZT k'
        lazy_list_0 = module_0.LazyList(str_0)
        var_0 = lazy_list_0.__iter__()

if __name__ == "__main__":
    unittest.main()
