import unittest
import timeout_decorator
import ansible.plugins.action.normal as module_0

class Test_Normal_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bool_0 = True
            list_0 = [bool_0, bool_0]
            set_0 = None
            int_0 = 292
            str_0 = 'n@L|UXe[v<qPa|\x0bgLjX'
            action_module_0 = module_0.ActionModule(list_0, bool_0, set_0, int_0, str_0, set_0)
            dict_0 = {bool_0: action_module_0, int_0: action_module_0}
            float_0 = 60.0
            tuple_0 = (action_module_0, dict_0, float_0)
            action_module_1 = module_0.ActionModule(bool_0, list_0, bool_0, tuple_0, list_0, float_0)
            var_0 = action_module_1.run()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
