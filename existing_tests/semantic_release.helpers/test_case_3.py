import unittest
import timeout_decorator
import semantic_release.helpers as module_0
import urllib3.util.retry as module_1

class Test_Helpers_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'subject'
        var_0 = module_0.format_arg(str_0)

if __name__ == "__main__":
    unittest.main()
