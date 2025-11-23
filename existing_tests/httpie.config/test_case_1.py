import unittest
import timeout_decorator
import httpie.config as module_0
import pathlib as module_1

class Test_Config_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            path_0 = module_0.get_default_config_dir()
            base_config_dict_0 = module_0.BaseConfigDict(path_0)
            path_1 = module_0.get_default_config_dir()
            bool_0 = base_config_dict_0.is_new()
            config_0 = module_0.Config(path_0)
            base_config_dict_1 = module_0.BaseConfigDict(path_1)
            path_2 = module_0.get_default_config_dir()
            var_0 = base_config_dict_0.save()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
