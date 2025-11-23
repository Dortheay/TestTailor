import unittest
import timeout_decorator
import apimd.loader as module_0

class Test_Loader_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = "w@EF\\'<a"
        str_1 = '2<\\8"vq*.dksB>^'
        iterator_0 = module_0.walk_packages(str_0, str_1)
        str_2 = '%C4As'
        bool_0 = None
        str_3 = 'u2B2K'
        dict_0 = {str_0: str_3}
        bool_1 = None
        int_0 = 2314
        bool_2 = True
        sequence_0 = module_0.gen_api(dict_0, str_2, toc=bool_2)
        bool_3 = True
        sequence_1 = module_0.gen_api(dict_0, link=bool_3, level=int_0, dry=bool_2)
        int_1 = 952
        sequence_2 = module_0.gen_api(dict_0, prefix=str_3, level=int_1, toc=bool_1, dry=bool_0)
        bool_4 = True
        str_4 = 'typing.Reversible'
        bool_5 = True
        int_2 = 12
        str_5 = module_0.loader(str_0, str_4, bool_5, int_2, bool_4)
        int_3 = 3189
        sequence_3 = module_0.gen_api(dict_0, level=int_3, toc=bool_3)

if __name__ == "__main__":
    unittest.main()
