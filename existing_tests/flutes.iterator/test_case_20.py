import unittest
import timeout_decorator
import flutes.iterator as module_0

class Test_Iterator_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            iterator_0 = None
            str_0 = 'mW!h!cDl'
            dict_0 = None
            str_1 = 'leave'
            str_2 = None
            str_3 = 'xh?>Y'
            dict_1 = {str_1: str_0, str_0: str_0, str_2: str_0, str_3: iterator_0}
            lazy_list_0 = module_0.LazyList(dict_1)
            var_0 = lazy_list_0.__getitem__(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
