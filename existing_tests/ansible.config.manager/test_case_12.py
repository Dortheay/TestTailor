import unittest
import timeout_decorator
import ansible.config.manager as module_0

class Test_Manager_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            dict_0 = None
            float_0 = None
            var_0 = module_0.get_ini_config_value(dict_0, float_0)
            str_0 = 'p4\x0b)q'
            config_manager_0 = module_0.ConfigManager()
            var_1 = config_manager_0.get_plugin_vars(str_0, str_0)
            var_2 = config_manager_0.update_config_data()
            var_3 = config_manager_0.get_configuration_definitions()
            int_0 = -1337
            var_4 = config_manager_0.get_plugin_vars(config_manager_0, int_0)
            float_1 = 817.8620233180316
            var_5 = config_manager_0.get_configuration_definition(float_1)
            bool_0 = True
            str_1 = '[[\rWi:BJ>B!X"w4)'
            var_6 = module_0.get_ini_config_value(config_manager_0, float_1)
            var_7 = config_manager_0.get_config_value(str_0, str_1, str_1, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
