import unittest
import timeout_decorator
import apimd.loader as module_0

class Test_Loader_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = "w@EF\\'<a"
            str_1 = '2<\\8"vq*.dksB>^'
            bool_0 = None
            str_2 = 'u22K'
            dict_0 = {str_0: str_2}
            bool_1 = None
            sequence_0 = module_0.gen_api(dict_0, str_1, link=bool_0, toc=bool_0, dry=bool_1)
            bool_2 = True
            str_3 = ''
            int_0 = 12
            bool_3 = True
            str_4 = module_0.loader(str_3, str_3, bool_2, int_0, bool_3)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
