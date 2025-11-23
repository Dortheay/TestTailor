import unittest
import timeout_decorator
import apimd.loader as module_0

class Test_Loader_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = 'r'
            str_1 = 'V pK3x)NxA=90)cl-'
            str_2 = 'tuple'
            str_3 = 'collections.abc.MutableMapping'
            dict_0 = {str_0: str_1, str_2: str_3}
            int_0 = 2681
            bool_0 = True
            str_4 = 'typing.Reversible'
            bool_1 = True
            str_5 = module_0.loader(str_3, str_4, bool_1, int_0, bool_0)
            sequence_0 = module_0.gen_api(dict_0, level=int_0, toc=bool_0, dry=bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
