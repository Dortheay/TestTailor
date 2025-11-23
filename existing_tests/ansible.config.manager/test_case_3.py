import unittest
import timeout_decorator
import ansible.config.manager as module_0

class Test_Manager_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            config_manager_0 = module_0.ConfigManager()
            config_manager_1 = module_0.ConfigManager(config_manager_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
