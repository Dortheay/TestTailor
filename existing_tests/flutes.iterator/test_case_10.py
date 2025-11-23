import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            iterable_0 = None
            lazy_list_0 = module_0.LazyList(iterable_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
