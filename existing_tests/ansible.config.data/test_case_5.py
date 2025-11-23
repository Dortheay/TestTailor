import unittest
import timeout_decorator
import ansible.config.data as module_0

class Test_Data_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            config_data_0 = module_0.ConfigData()
            var_0 = config_data_0.get_settings()
            str_0 = '\rzgg7/crNouR/'
            var_1 = config_data_0.get_settings(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
