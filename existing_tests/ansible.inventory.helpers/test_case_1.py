import unittest
import timeout_decorator
import ansible.inventory.helpers as module_0

class Test_Helpers_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            bytes_0 = None
            var_0 = module_0.get_group_vars(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
