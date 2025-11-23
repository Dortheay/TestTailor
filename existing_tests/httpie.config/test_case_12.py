import unittest
import timeout_decorator
import httpie.config as module_0

class Test_Config_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        path_0 = module_0.get_default_config_dir()

if __name__ == "__main__":
    unittest.main()
