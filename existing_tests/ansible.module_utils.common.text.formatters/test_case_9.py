import unittest
import timeout_decorator
import ansible.module_utils.common.text.formatters as module_0

class Test_Formatters_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = 'MG\n9/%y=A@!|>U#'
        var_0 = module_0.lenient_lowercase(str_0)

if __name__ == "__main__":
    unittest.main()
