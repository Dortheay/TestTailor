import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            bytes_0 = None
            int_0 = 4442
            iterator_0 = module_0.chunk(int_0, int_0)
            lazy_list_0 = module_0.LazyList(iterator_0)
            var_0 = lazy_list_0.__getitem__(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
