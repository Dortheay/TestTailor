import unittest
import timeout_decorator
import ansible.module_utils.facts.utils as module_0

class Test_Utils_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bool_0 = False
            var_0 = module_0.get_file_lines(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
