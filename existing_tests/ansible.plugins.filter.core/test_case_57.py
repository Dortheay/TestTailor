import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_58(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        var_0 = module_0.regex_replace()

if __name__ == "__main__":
    unittest.main()
