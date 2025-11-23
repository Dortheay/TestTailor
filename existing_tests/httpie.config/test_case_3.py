import unittest
import timeout_decorator
import httpie.config as module_0
import pathlib as module_1

class Test_Config_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            path_0 = module_0.get_default_config_dir()
            config_file_error_0 = module_0.ConfigFileError()
            config_0 = module_0.Config()
            base_config_dict_0 = module_0.BaseConfigDict(path_0)
            var_0 = base_config_dict_0.delete()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
