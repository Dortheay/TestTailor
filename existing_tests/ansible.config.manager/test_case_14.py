import unittest
import timeout_decorator
import ansible.config.manager as module_0

class Test_Manager_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'o'
        float_0 = -1522.7
        var_0 = module_0.get_ini_config_value(str_0, float_0)
        config_manager_0 = module_0.ConfigManager()

if __name__ == "__main__":
    unittest.main()
