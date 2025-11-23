import unittest
import timeout_decorator
import ansible.config.data as module_0

class Test_Data_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        config_data_0 = module_0.ConfigData()
        var_0 = config_data_0.get_settings()

if __name__ == "__main__":
    unittest.main()
