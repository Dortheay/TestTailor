import unittest
import timeout_decorator
import ansible.config.manager as module_0

class Test_Manager_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        config_manager_0 = module_0.ConfigManager()

if __name__ == "__main__":
    unittest.main()
