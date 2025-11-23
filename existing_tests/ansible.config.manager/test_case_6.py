import unittest
import timeout_decorator
import ansible.config.manager as module_0

class Test_Manager_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            str_0 = 'dict'
            list_0 = [str_0, str_0]
            config_manager_0 = module_0.ConfigManager()
            var_0 = config_manager_0.update_config_data(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
