import unittest
import timeout_decorator
import thefuck.conf as module_0

class Test_Conf_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        settings_0 = module_0.Settings()

if __name__ == "__main__":
    unittest.main()
