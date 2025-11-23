import unittest
import timeout_decorator
import ansible.config.manager as module_0

class Test_Manager_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = 'tBenP'
        list_0 = [str_0, str_0, str_0, str_0]
        str_1 = '-RgSM9'
        var_0 = module_0.get_ini_config_value(list_0, str_1)
        config_manager_0 = module_0.ConfigManager()
        setting_0 = module_0.Setting(*list_0)
        bool_0 = False
        var_1 = config_manager_0.get_configuration_definition(setting_0, bool_0)
        var_2 = config_manager_0.get_configuration_definitions(str_0)

if __name__ == "__main__":
    unittest.main()
