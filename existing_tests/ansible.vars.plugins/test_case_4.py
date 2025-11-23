import unittest
import timeout_decorator
import ansible.vars.plugins as module_0
import ansible.inventory.host as module_1

class Test_Plugins_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            complex_0 = None
            bool_0 = None
            int_0 = -2203
            list_0 = []
            dict_0 = {int_0: bool_0, bool_0: int_0, complex_0: list_0, int_0: bool_0}
            float_0 = 889.7
            str_0 = ',Qh^qY8_Pt'
            var_0 = module_0.get_plugin_vars(dict_0, float_0, str_0, list_0)
            bool_1 = True
            host_0 = module_1.Host()
            int_1 = -1957
            var_1 = module_0.get_vars_from_path(bool_0, bool_1, host_0, int_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
