import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_34(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_21(self):
        str_0 = '!exclude_this'
        str_1 = '&intersect_this'
        str_2 = 'regular_pattern'
        var_0 = None
        var_1 = [str_0, str_1, str_2, var_0, str_2]
        var_2 = module_0.order_patterns(var_1)

if __name__ == "__main__":
    unittest.main()
