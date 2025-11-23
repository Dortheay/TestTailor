import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_66(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        complex_0 = None
        list_0 = [complex_0]
        var_0 = module_0.combine(*list_0)
        list_1 = None
        var_1 = module_0.quote(list_1)

if __name__ == "__main__":
    unittest.main()
