import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_56(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        list_0 = None
        var_0 = module_0.quote(list_0)

if __name__ == "__main__":
    unittest.main()
