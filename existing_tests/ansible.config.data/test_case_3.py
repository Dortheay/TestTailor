import unittest
import timeout_decorator
import ansible.config.data as module_0

class Test_Data_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        config_data_0 = module_0.ConfigData()
        str_0 = 'MockPlugin'
        var_0 = ()
        str_1 = 'type'
        str_2 = 'name'
        str_3 = 'mock_type'
        str_4 = 'mock_name'
        str_5 = {str_1: str_3, str_2: str_4}
        var_1 = type(str_0, var_0, str_5)
        var_2 = config_data_0.get_settings()
        var_3 = len(var_2)
        var_4 = config_data_0.get_settings(var_1)
        var_5 = len(var_4)
        str_6 = 'NonexistentPlugin'
        var_6 = ()
        str_7 = 'nonexistent_type'
        str_8 = 'nonexistent_name'
        str_9 = {str_1: str_7, str_2: str_8}
        var_7 = type(str_6, var_6, str_9)
        var_8 = config_data_0.get_settings(var_7)

if __name__ == "__main__":
    unittest.main()
