import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            float_0 = 0.1
            bytes_0 = b'\xab\xbc\xbfy\xb6"o\xe9\xb1P|\\\x8eLf!\x7f\xa7Y\xdb'
            list_0 = [float_0, float_0]
            iterator_0 = module_0.drop_until(bytes_0, list_0)
            set_0 = set()
            str_0 = '0>|#s^(L^3t<B\\iX1b>'
            lazy_list_0 = module_0.LazyList(str_0)
            lazy_list_1 = module_0.LazyList(set_0)
            float_1 = 1584.19828
            str_1 = 'O'
            map_list_0 = module_0.MapList(float_1, str_1)
            iterator_1 = map_list_0.__iter__()
            lazy_list_2 = module_0.LazyList(iterator_1)
            range_0 = module_0.Range(*list_0)
            int_0 = range_0.__len__()
            var_0 = lazy_list_1.__iter__()
            map_list_1 = module_0.MapList(float_0, lazy_list_2)
            var_1 = map_list_1.__getitem__(lazy_list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
