import unittest
import timeout_decorator
import pytutils.files as module_0

class Test_Files_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            str_0 = '!Ff{hZ'
            float_0 = -2257.0
            var_0 = module_0.burp(str_0, float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
