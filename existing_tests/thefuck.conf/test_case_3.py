import unittest
import timeout_decorator
import thefuck.conf as module_0

class Test_Conf_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = True
            settings_0 = module_0.Settings()
            var_0 = settings_0.init(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
