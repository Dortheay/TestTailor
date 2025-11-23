import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_55(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = 'S}/K6\r2&`H\x0cMMxu+\x0c'
        var_0 = module_0.quote(str_0)

if __name__ == "__main__":
    unittest.main()
