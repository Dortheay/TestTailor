import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            int_0 = None
            iterable_0 = None
            iterator_0 = module_0.chunk(int_0, iterable_0)
            bool_0 = False
            list_0 = [bool_0]
            range_0 = module_0.Range(*list_0)
            var_0 = range_0.__getitem__(iterator_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
