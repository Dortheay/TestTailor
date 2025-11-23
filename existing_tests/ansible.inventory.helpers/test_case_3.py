import unittest
import timeout_decorator
import ansible.inventory.helpers as module_0

class Test_Helpers_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        set_0 = set()
        var_0 = module_0.get_group_vars(set_0)

if __name__ == "__main__":
    unittest.main()
