import unittest
import timeout_decorator
import pytutils.log as module_0

class Test_Log_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = '#'
            var_0 = module_0.configure(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
