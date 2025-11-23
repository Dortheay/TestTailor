import unittest
import timeout_decorator
import thefuck.rules.no_such_file as module_0

class Test_No_such_file_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            dict_0 = {}
            var_0 = module_0.match(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
