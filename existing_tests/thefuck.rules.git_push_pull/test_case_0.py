import unittest
import timeout_decorator
import thefuck.rules.git_push_pull as module_0

class Test_Git_push_pull_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            set_0 = set()
            var_0 = module_0.get_new_command(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
