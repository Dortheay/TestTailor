import unittest
import timeout_decorator
import httpie.config as module_0
import pathlib as module_1

class Test_Config_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            path_0 = None
            base_config_dict_0 = module_0.BaseConfigDict(path_0)
            var_0 = base_config_dict_0.load()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
