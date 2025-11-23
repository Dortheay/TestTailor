import unittest
import timeout_decorator
import ansible.parsing.quoting as module_0

class Test_Quoting_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = 245
            var_0 = module_0.is_quoted(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
