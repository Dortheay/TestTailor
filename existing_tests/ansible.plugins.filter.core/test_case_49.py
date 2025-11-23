import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_50(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        bool_0 = True
        var_0 = module_0.get_hash(bool_0)

if __name__ == "__main__":
    unittest.main()
