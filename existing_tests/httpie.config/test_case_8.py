import unittest
import timeout_decorator
import httpie.config as module_0
import pathlib as module_1

class Test_Config_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            str_0 = ''
            list_0 = [str_0, str_0, str_0]
            path_0 = module_1.Path(*list_0)
            base_config_dict_0 = module_0.BaseConfigDict(path_0)
            bool_0 = base_config_dict_0.is_new()
            var_0 = base_config_dict_0.ensure_directory()
            path_1 = module_0.get_default_config_dir()
            base_config_dict_1 = module_0.BaseConfigDict(path_1)
            var_1 = base_config_dict_1.load()
            path_2 = module_0.get_default_config_dir()
            base_config_dict_2 = module_0.BaseConfigDict(path_2)
            var_2 = base_config_dict_2.save()
            base_config_dict_3 = module_0.BaseConfigDict(path_2)
            bool_1 = base_config_dict_3.is_new()
            config_0 = module_0.Config(path_1)
            str_1 = None
            float_0 = -751.46
            base_config_dict_4 = module_0.BaseConfigDict(path_2)
            list_1 = [base_config_dict_4, var_2, var_2, base_config_dict_2]
            tuple_0 = (float_0, list_1)
            dict_0 = {str_1: str_1, str_1: tuple_0}
            var_3 = path_1.write_text(config_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
