import unittest
import timeout_decorator
import httpie.config as module_0
import pathlib as module_1

class Test_Config_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            str_0 = 'kL*Z%pg*x-]$&\\q=:Y'
            list_0 = [str_0, str_0, str_0, str_0]
            path_0 = module_1.Path(*list_0)
            base_config_dict_0 = module_0.BaseConfigDict(path_0)
            bool_0 = base_config_dict_0.is_new()
            var_0 = base_config_dict_0.delete()
            path_1 = module_0.get_default_config_dir()
            base_config_dict_1 = module_0.BaseConfigDict(path_1)
            bool_1 = base_config_dict_1.is_new()
            var_1 = base_config_dict_1.ensure_directory()
            path_2 = module_0.get_default_config_dir()
            base_config_dict_2 = module_0.BaseConfigDict(path_2)
            bytes_0 = b'.\xc9\xbd\x9ak\xbc\xceI\xce?N\xad\x05'
            var_2 = base_config_dict_2.save(bytes_0)
            var_3 = base_config_dict_2.load()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
