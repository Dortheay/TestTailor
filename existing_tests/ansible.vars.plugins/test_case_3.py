import unittest
import timeout_decorator
import ansible.vars.plugins as module_0
import ansible.inventory.host as module_1

class Test_Plugins_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bool_0 = True
            str_0 = 'a^5&l;'
            float_0 = -3779.9
            list_0 = [float_0, str_0, float_0]
            int_0 = -381
            var_0 = module_0.get_plugin_vars(bool_0, str_0, list_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
