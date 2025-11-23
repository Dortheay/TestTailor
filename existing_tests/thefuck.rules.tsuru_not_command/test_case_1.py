import unittest
import timeout_decorator
import thefuck.rules.tsuru_not_command as module_0

class Test_Tsuru_not_command_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            list_0 = []
            var_0 = module_0.get_new_command(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
