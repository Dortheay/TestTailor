import unittest
import timeout_decorator
import ansible.utils.vars as module_0

class Test_Vars_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            bool_0 = True
            float_0 = 2651.0
            str_0 = ''
            tuple_0 = (str_0, float_0)
            var_0 = module_0._isidentifier_PY3(tuple_0)
            bool_1 = True
            bytes_0 = b'\xae;\x85\x97\xd8\x1b\x18k)\xb9$|\x19\x05\x96\xe3[\x98\x1b'
            var_1 = module_0._isidentifier_PY3(bytes_0)
            var_2 = module_0.get_unique_id()
            bool_2 = True
            tuple_1 = (bool_0, float_0, bool_1, bool_2)
            dict_0 = {}
            bytes_1 = b'\xb0\xa6)\xbe\xab'
            var_3 = module_0.load_options_vars(bytes_1)
            int_0 = None
            set_0 = set()
            tuple_2 = (int_0, set_0)
            var_4 = module_0.merge_hash(dict_0, dict_0, tuple_2)
            bool_3 = True
            var_5 = module_0.load_options_vars(bool_3)
            var_6 = module_0.get_unique_id()
            var_7 = module_0.merge_hash(bool_2, tuple_1, bool_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
