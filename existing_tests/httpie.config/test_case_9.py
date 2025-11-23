import unittest
import timeout_decorator
import httpie.config as module_0
import pathlib as module_1

class Test_Config_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            path_0 = module_0.get_default_config_dir()
            base_config_dict_0 = module_0.BaseConfigDict(path_0)
            var_0 = base_config_dict_0.load()
            path_1 = module_0.get_default_config_dir()
            base_config_dict_1 = module_0.BaseConfigDict(path_1)
            var_1 = base_config_dict_1.save()
            base_config_dict_2 = module_0.BaseConfigDict(path_1)
            bool_0 = base_config_dict_2.is_new()
            config_0 = module_0.Config(path_0)
            str_0 = None
            float_0 = -751.46
            base_config_dict_3 = module_0.BaseConfigDict(path_1)
            list_0 = [base_config_dict_3, var_1, var_1, base_config_dict_1]
            tuple_0 = (float_0, list_0)
            dict_0 = {str_0: str_0, str_0: tuple_0}
            var_2 = path_0.write_text(config_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
