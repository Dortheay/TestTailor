import unittest
import timeout_decorator
import ansible.utils.vars as module_0

class Test_Vars_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            float_0 = 1162.0
            var_0 = module_0.get_unique_id()
            var_1 = module_0._isidentifier_PY3(float_0)
            str_0 = 'hFwPbV'
            var_2 = module_0._isidentifier_PY3(str_0)
            tuple_0 = ()
            var_3 = module_0.load_options_vars(tuple_0)
            var_4 = module_0.load_extra_vars(str_0)
            bytes_0 = b'\xe9\xf3\xba.<Z'
            var_5 = module_0.combine_vars(bytes_0, tuple_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
