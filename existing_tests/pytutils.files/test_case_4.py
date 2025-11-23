import unittest
import timeout_decorator
import pytutils.files as module_0

class Test_Files_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            str_0 = '-'
            var_0 = module_0.islurp(str_0)
            var_1 = list(var_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
