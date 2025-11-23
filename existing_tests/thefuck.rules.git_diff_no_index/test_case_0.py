import unittest
import timeout_decorator
import thefuck.rules.git_diff_no_index as module_0

class Test_Git_diff_no_index_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            dict_0 = {}
            var_0 = module_0.get_new_command(dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
