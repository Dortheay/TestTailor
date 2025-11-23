import unittest
import timeout_decorator
import ansible.utils.vars as module_0

class Test_Vars_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            float_0 = 2651.0
            str_0 = ''
            tuple_0 = (str_0, float_0)
            bytes_0 = b'\xae;\x85\x97\xd8\x1b\x18k)\xb9$|\x19\x05\x96\xe3[\x98\x1b'
            var_0 = module_0._isidentifier_PY3(bytes_0)
            var_1 = module_0.get_unique_id()
            dict_0 = {}
            bytes_1 = b'\xb0\xa6)\xbe\xab'
            var_2 = module_0.load_options_vars(bytes_1)
            set_0 = set()
            var_3 = module_0.load_extra_vars(tuple_0)
            str_1 = 'f:0v.\r9\x0b<08f -'
            var_4 = module_0.combine_vars(dict_0, str_1, set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
