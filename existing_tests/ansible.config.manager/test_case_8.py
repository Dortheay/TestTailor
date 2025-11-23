import unittest
import timeout_decorator
import ansible.config.manager as module_0

class Test_Manager_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            dict_0 = None
            config_manager_0 = module_0.ConfigManager()
            var_0 = config_manager_0.update_config_data()
            str_0 = None
            set_0 = {var_0}
            var_1 = config_manager_0.get_plugin_vars(str_0, set_0)
            int_0 = -1337
            var_2 = config_manager_0.get_plugin_vars(config_manager_0, int_0)
            float_0 = -1155.76
            var_3 = module_0.get_ini_config_value(dict_0, float_0)
            list_0 = [float_0, var_3]
            int_1 = 8192
            var_4 = config_manager_0.get_config_value(list_0, int_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
