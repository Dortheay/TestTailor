import unittest
import timeout_decorator
import thefuck.system.unix as module_0

class Test_Unix_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            dict_0 = {}
            var_0 = module_0.open_command(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
