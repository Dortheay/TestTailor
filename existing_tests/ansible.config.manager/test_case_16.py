import unittest
import timeout_decorator
import ansible.config.manager as module_0

class Test_Manager_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        config_manager_0 = module_0.ConfigManager()
        var_0 = config_manager_0.update_config_data()
        str_0 = '$Mg]d'
        var_1 = config_manager_0.get_configuration_definition(str_0)
        int_0 = None
        var_2 = config_manager_0.get_plugin_options(int_0, config_manager_0)

if __name__ == "__main__":
    unittest.main()
