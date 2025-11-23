import unittest
import timeout_decorator
import ansible.config.manager as module_0

class Test_Manager_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        str_0 = 'tBenP'
        list_0 = [str_0, str_0, str_0, str_0]
        str_1 = '-RgSM9'
        var_0 = module_0.get_ini_config_value(list_0, str_1)
        config_manager_0 = module_0.ConfigManager()
        var_1 = config_manager_0.get_configuration_definitions(str_0)

if __name__ == "__main__":
    unittest.main()
