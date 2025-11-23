import unittest
import timeout_decorator
import ansible.config.manager as module_0

class Test_Manager_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        dict_0 = None
        float_0 = None
        var_0 = module_0.get_ini_config_value(dict_0, float_0)
        str_0 = 'p4\x0b)q'
        config_manager_0 = module_0.ConfigManager()
        var_1 = config_manager_0.get_plugin_vars(str_0, str_0)
        var_2 = config_manager_0.update_config_data()
        var_3 = config_manager_0.get_configuration_definitions()
        float_1 = 817.688
        var_4 = config_manager_0.get_configuration_definition(float_1)
        var_5 = module_0.get_ini_config_value(config_manager_0, float_1)

if __name__ == "__main__":
    unittest.main()
