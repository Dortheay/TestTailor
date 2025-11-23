import unittest
import timeout_decorator
import ansible.inventory.helpers as module_0

class Test_Helpers_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            str_0 = 'IZC$sM6.\x0c'
            var_0 = module_0.get_group_vars(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
