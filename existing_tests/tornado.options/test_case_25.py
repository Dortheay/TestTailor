import unittest
import timeout_decorator
import tornado.options as module_0
import builtins as module_1

class Test_Options_26(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_19(self):
        try:
            list_0 = module_0.parse_command_line()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
