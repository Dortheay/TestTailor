import unittest
import timeout_decorator
import pytutils.env as module_0

class Test_Env_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = ',etP19R3lK3XHQ%'
            str_1 = 'cP=?Hg'
            str_2 = module_0.expand(str_1)
            set_0 = {str_0, str_0}
            ordered_dict_0 = module_0.load_env_file(set_0)
            generator_0 = module_0.parse_env_file_contents()
            bool_0 = True
            ordered_dict_1 = module_0.load_env_file(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
