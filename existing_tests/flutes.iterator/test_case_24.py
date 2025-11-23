import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            float_0 = 0.1
            list_0 = [float_0, float_0]
            iterable_0 = None
            iterator_0 = module_0.drop_until(float_0, iterable_0)
            set_0 = set()
            lazy_list_0 = module_0.LazyList(set_0)
            range_0 = module_0.Range(*list_0)
            var_0 = range_0.__getitem__(float_0)
            var_1 = lazy_list_0.__iter__()
            map_list_0 = module_0.MapList(float_0, lazy_list_0)
            int_0 = -571
            iterator_1 = module_0.drop(int_0, iterable_0)
            int_1 = range_0.__next__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
