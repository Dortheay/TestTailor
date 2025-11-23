import unittest
import timeout_decorator
import ansible.config.manager as module_0

class Test_Manager_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        config_manager_0 = module_0.ConfigManager()
        var_0 = config_manager_0.update_config_data()
        var_1 = module_0.find_ini_config_file()

if __name__ == "__main__":
    unittest.main()
