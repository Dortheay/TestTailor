import unittest
import timeout_decorator
import httpie.config as module_0
import pathlib as module_1

class Test_Config_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            str_0 = '/custom/config/dir'
            list_0 = [str_0]
            path_0 = module_1.Path(*list_0)
            base_config_dict_0 = module_0.BaseConfigDict(path_0)
            var_0 = base_config_dict_0.ensure_directory()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
