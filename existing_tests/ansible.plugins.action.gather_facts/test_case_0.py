import unittest
import timeout_decorator
import ansible.plugins.action.gather_facts as module_0

class Test_Gather_facts_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'zeidEz>~yV'
            dict_0 = {str_0: str_0}
            int_0 = -93
            bytes_0 = b'[k\xf6/a\xc0'
            set_0 = {bytes_0, str_0, str_0, bytes_0}
            list_0 = [str_0, dict_0]
            bool_0 = True
            tuple_0 = (bytes_0,)
            action_module_0 = module_0.ActionModule(set_0, list_0, bytes_0, bool_0, tuple_0, set_0)
            float_0 = 2884.60451
            bool_1 = False
            action_module_1 = module_0.ActionModule(dict_0, int_0, bytes_0, action_module_0, float_0, bool_1)
            var_0 = action_module_1.run()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
