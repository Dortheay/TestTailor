import unittest
import timeout_decorator
import ansible.utils.helpers as module_0

class Test_Helpers_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        float_0 = 245.0
        list_0 = None
        var_0 = module_0.pct_to_int(float_0, list_0)

if __name__ == "__main__":
    unittest.main()
