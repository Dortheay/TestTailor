import unittest
import timeout_decorator
import httpie.config as module_0
import pathlib as module_1

class Test_Config_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            path_0 = module_1.Path()
            path_1 = module_0.get_default_config_dir()
            var_0 = path_1.is_fifo()
            base_config_dict_0 = module_0.BaseConfigDict(path_0)
            config_0 = module_0.Config()
            base_config_dict_1 = module_0.BaseConfigDict(path_0)
            var_1 = base_config_dict_0.save(base_config_dict_0)
            var_2 = base_config_dict_1.delete()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
