import unittest
import timeout_decorator
import httpie.config as module_0

class Test_Config_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        config_0 = module_0.Config()

if __name__ == "__main__":
    unittest.main()
