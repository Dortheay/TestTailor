import unittest
import timeout_decorator
import apimd.loader as module_0

class Test_Loader_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = "w@EF\\'<a"
        str_1 = '2<\\8"vq*.dksB>^'
        str_2 = 'jnY0!}4'
        bool_0 = None
        str_3 = 'u22K'
        dict_0 = {str_0: str_3}
        bool_1 = None
        sequence_0 = module_0.gen_api(dict_0, str_1, link=bool_0, toc=bool_0, dry=bool_1)
        int_0 = 2301
        bool_2 = True
        sequence_1 = module_0.gen_api(dict_0, str_3, toc=bool_2)
        bool_3 = False
        str_4 = module_0.loader(str_2, str_0, bool_0, int_0, bool_3)

if __name__ == "__main__":
    unittest.main()
