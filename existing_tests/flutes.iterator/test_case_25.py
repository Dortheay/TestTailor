import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        try:
            int_0 = 285
            str_0 = '`n` should be positive'
            int_1 = -979
            iterable_0 = None
            iterator_0 = module_0.take(int_1, iterable_0)
            map_list_0 = None
            tuple_0 = (map_list_0,)
            var_0 = module_0.scanr(iterator_0, tuple_0)
            iterator_1 = module_0.chunk(int_0, str_0)
            range_0 = module_0.Range()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
