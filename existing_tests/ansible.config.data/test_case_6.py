import unittest
import timeout_decorator
import ansible.config.data as module_0

class Test_Data_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            config_data_0 = module_0.ConfigData()
            int_0 = 1560
            var_0 = config_data_0.get_setting(int_0)
            float_0 = 0.001
            list_0 = [float_0]
            var_1 = config_data_0.update_setting(float_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
