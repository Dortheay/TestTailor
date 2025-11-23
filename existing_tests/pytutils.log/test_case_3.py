import unittest
import timeout_decorator
import pytutils.log as module_0

class Test_Log_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            var_0 = module_0.get_config()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
