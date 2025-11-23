import unittest
import timeout_decorator
import httpie.config as module_0
import pathlib as module_1

class Test_Config_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            path_0 = module_0.get_default_config_dir()
            config_file_error_0 = module_0.ConfigFileError()
            path_1 = None
            base_config_dict_0 = module_0.BaseConfigDict(path_1)
            base_config_dict_1 = module_0.BaseConfigDict(path_0)
            base_config_dict_2 = module_0.BaseConfigDict(path_1)
            config_0 = module_0.Config()
            base_config_dict_3 = module_0.BaseConfigDict(path_0)
            var_0 = base_config_dict_3.save(config_0)
            var_1 = base_config_dict_0.delete()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
