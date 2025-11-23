import unittest
import timeout_decorator
import thefuck.conf as module_0

class Test_Conf_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        settings_0 = module_0.Settings()
        var_0 = settings_0.init()

if __name__ == "__main__":
    unittest.main()
