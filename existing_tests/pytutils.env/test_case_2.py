import unittest
import timeout_decorator
import pytutils.env as module_0

class Test_Env_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'o9k=]XszM^"cx'
            list_0 = [str_0]
            mutable_mapping_0 = None
            ordered_dict_0 = module_0.load_env_file(list_0, mutable_mapping_0)
            str_1 = '9cu>8eWQ]G _&Yc6\tAn'
            str_2 = module_0.expand(str_1)
            ordered_dict_1 = module_0.load_env_file(list_0)
            iterable_0 = None
            ordered_dict_2 = module_0.load_env_file(iterable_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
