import unittest
import timeout_decorator
import ansible.plugins.action.set_stats as module_0

class Test_Set_stats_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = True
            tuple_0 = ()
            set_0 = {tuple_0}
            list_0 = [tuple_0]
            dict_0 = {}
            int_0 = 1129
            float_0 = 2.0
            action_module_0 = module_0.ActionModule(set_0, list_0, dict_0, int_0, float_0, float_0)
            var_0 = action_module_0.run(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
