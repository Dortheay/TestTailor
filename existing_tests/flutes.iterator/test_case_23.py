import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_24(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_15(self):
        try:
            float_0 = 0.1
            bytes_0 = b'\xab\xbc\xbfy\xb6"o\xe9\xb1P|\\\x8eLf!\x7f\xa7Y\xdb'
            list_0 = [float_0, float_0]
            iterable_0 = None
            iterator_0 = module_0.drop_until(float_0, iterable_0)
            iterator_1 = module_0.drop_until(bytes_0, list_0)
            set_0 = set()
            lazy_list_0 = module_0.LazyList(set_0)
            var_0 = lazy_list_0.__iter__()
            float_1 = 1584.19828
            str_0 = 'O'
            map_list_0 = module_0.MapList(float_1, str_0)
            int_0 = 1090
            var_1 = map_list_0.__getitem__(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
