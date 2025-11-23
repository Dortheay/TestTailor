import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            str_0 = "ulj4N'v<tgu%"
            lazy_list_0 = module_0.LazyList(str_0)
            var_0 = lazy_list_0.__len__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
