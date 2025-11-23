import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_53(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        str_0 = ''
        var_0 = module_0.to_bool(str_0)

if __name__ == "__main__":
    unittest.main()
