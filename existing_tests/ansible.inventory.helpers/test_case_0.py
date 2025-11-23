import unittest
import timeout_decorator
import ansible.inventory.helpers as module_0

class Test_Helpers_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            float_0 = None
            var_0 = module_0.sort_groups(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
