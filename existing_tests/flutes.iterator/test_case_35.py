import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_36(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_27(self):
        try:
            int_0 = 10
            var_0 = range(int_0)
            lazy_list_0 = module_0.LazyList(var_0)
            var_1 = list(lazy_list_0)
            iterable_0 = None
            iterator_0 = module_0.drop(int_0, iterable_0)
            sequence_0 = None
            map_list_0 = module_0.MapList(iterator_0, sequence_0)
            bool_0 = None
            var_2 = lazy_list_0.__getitem__(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
