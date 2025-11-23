import unittest
import timeout_decorator
import ansible.plugins.action.set_stats as module_0

class Test_Set_stats_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bool_0 = False
            set_0 = {bool_0}
            str_0 = 'Xm_ ??EF6{'
            bool_1 = False
            str_1 = 'system-serial-number'
            float_0 = -432.63
            int_0 = 2796
            dict_0 = {}
            list_0 = None
            bool_2 = False
            action_module_0 = module_0.ActionModule(list_0, list_0, bool_2, dict_0, dict_0, int_0)
            action_module_1 = module_0.ActionModule(dict_0, int_0, action_module_0, float_0, set_0, list_0)
            tuple_0 = (float_0, int_0, action_module_1)
            str_2 = ";[\x0c'{a0"
            action_module_2 = module_0.ActionModule(str_1, tuple_0, str_2, set_0, list_0, dict_0)
            var_0 = action_module_2.run(str_0, bool_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
