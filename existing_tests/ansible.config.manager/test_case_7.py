import unittest
import timeout_decorator
import ansible.config.manager as module_0

class Test_Manager_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            config_manager_0 = module_0.ConfigManager()
            str_0 = '$Mg]d'
            var_0 = config_manager_0.get_configuration_definition(str_0)
            float_0 = -278.84028
            str_1 = 'wH8LB_rW00:;|'
            config_manager_1 = module_0.ConfigManager(float_0, str_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
