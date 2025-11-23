import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = None
            dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
            str_1 = '!`28RlQ'
            map_list_0 = module_0.MapList(dict_0, str_1)
            int_0 = map_list_0.__len__()
            bytes_0 = b'7S'
            lazy_list_0 = module_0.LazyList(bytes_0)
            var_0 = lazy_list_0.__len__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
