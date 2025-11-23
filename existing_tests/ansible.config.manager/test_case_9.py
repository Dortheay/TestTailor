import unittest
import timeout_decorator
import ansible.config.manager as module_0

class Test_Manager_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            int_0 = None
            config_manager_0 = module_0.ConfigManager()
            var_0 = config_manager_0.get_configuration_definition(int_0)
            str_0 = '"ZA1l45'
            tuple_0 = None
            str_1 = ' w-s&=^?:v?\x0bU^Qa?'
            config_manager_1 = None
            dict_0 = {str_1: config_manager_1}
            var_1 = config_manager_0.initialize_plugin_configuration_definitions(str_0, tuple_0, dict_0)
            bool_0 = False
            var_2 = config_manager_0.get_configuration_definition(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
