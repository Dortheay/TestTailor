import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            float_0 = 1584.0025865747486
            str_0 = 'O'
            map_list_0 = module_0.MapList(float_0, str_0)
            iterator_0 = map_list_0.__iter__()
            iterator_1 = map_list_0.__iter__()
            lazy_list_0 = module_0.LazyList(iterator_0)
            var_0 = map_list_0.__getitem__(lazy_list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
