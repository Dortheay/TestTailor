import unittest
import timeout_decorator
import ansible.utils.color as module_0

class Test_Color_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '_ansible_ignore_errors'
            set_0 = {str_0, str_0}
            bool_0 = False
            str_1 = '^#sWJ1$>\nw]}#]\n'
            bool_1 = False
            set_1 = None
            dict_0 = {bool_0: str_0, str_1: set_0, str_0: set_0, set_1: set_0}
            str_2 = 'if address'
            tuple_0 = (dict_0, str_2, dict_0, str_2)
            var_0 = module_0.hostcolor(dict_0, tuple_0, str_1)
            list_0 = [str_0, bool_1, str_0]
            float_0 = -1036.011502
            var_1 = module_0.stringc(list_0, tuple_0, tuple_0)
            var_2 = module_0.colorize(str_1, bool_1, float_0)
            var_3 = module_0.parsecolor(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
