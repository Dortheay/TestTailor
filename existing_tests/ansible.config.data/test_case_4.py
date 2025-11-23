import unittest
import timeout_decorator
import ansible.config.data as module_0

class Test_Data_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = True
            config_data_0 = module_0.ConfigData()
            var_0 = config_data_0.get_setting(bool_0, bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
