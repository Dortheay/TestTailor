import unittest
import timeout_decorator
import ansible.utils.vars as module_0

class Test_Vars_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            var_0 = module_0.get_unique_id()
            var_1 = module_0.get_unique_id()
            float_0 = 0.0
            var_2 = module_0._isidentifier_PY3(float_0)
            var_3 = module_0.load_extra_vars(float_0)
            str_0 = 'ERROR: modified files exist in the repository.'
            var_4 = module_0.load_options_vars(str_0)
            var_5 = module_0.get_unique_id()
            var_6 = module_0.get_unique_id()
            float_1 = -1968.4417
            var_7 = module_0.load_extra_vars(float_1)
            var_8 = module_0.get_unique_id()
            bytes_0 = b'\xcbU@!\x10*\xa4/\xcf\xf7\xd7qD\xa5\tr\xa6\x80'
            int_0 = 22
            list_0 = [int_0, int_0, int_0, bytes_0]
            var_9 = module_0.get_unique_id()
            var_10 = module_0.load_extra_vars(bytes_0)
            var_11 = module_0.load_options_vars(str_0)
            var_12 = module_0.merge_hash(bytes_0, int_0, int_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
