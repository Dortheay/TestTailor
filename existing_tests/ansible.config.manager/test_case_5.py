import unittest
import timeout_decorator
import ansible.config.manager as module_0

class Test_Manager_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = 'kv`2q1zY9ylnFfJSYWP#'
            config_manager_0 = module_0.ConfigManager()
            var_0 = config_manager_0.get_configuration_definition(str_0, config_manager_0)
            float_0 = 512.0
            float_1 = -119.0
            var_1 = module_0.ensure_type(float_0, float_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
