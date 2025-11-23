import unittest
import timeout_decorator
import ansible.config.manager as module_0

class Test_Manager_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            str_0 = 'p4\x0b)q'
            config_manager_0 = module_0.ConfigManager()
            var_0 = config_manager_0.get_plugin_vars(str_0, str_0)
            var_1 = config_manager_0.update_config_data()
            int_0 = -1337
            var_2 = config_manager_0.get_plugin_vars(config_manager_0, int_0)
            float_0 = 817.688
            var_3 = config_manager_0.get_configuration_definition(float_0)
            var_4 = config_manager_0.get_config_value(str_0, str_0, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
