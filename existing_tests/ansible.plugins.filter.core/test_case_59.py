import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_60(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        list_0 = []
        bool_0 = True
        var_0 = module_0.from_yaml(bool_0)
        var_1 = module_0.quote(list_0)

if __name__ == "__main__":
    unittest.main()
