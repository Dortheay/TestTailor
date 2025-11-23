import unittest
import timeout_decorator
import ansible.config.data as module_0

class Test_Data_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            config_data_0 = module_0.ConfigData()
            str_0 = 'Bte1PfDnLYNW2'
            var_0 = config_data_0.update_setting(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
