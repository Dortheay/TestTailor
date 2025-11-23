import unittest
import timeout_decorator
import ansible.plugins.filter.core as module_0

class Test_Core_70(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_20(self):
        float_0 = 13.739070690504445
        str_0 = 'vmb|\n|u@'
        var_0 = module_0.regex_search(float_0, str_0)

if __name__ == "__main__":
    unittest.main()
