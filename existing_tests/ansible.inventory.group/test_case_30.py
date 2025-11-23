import unittest
import timeout_decorator
import ansible.inventory.group as module_0

class Test_Group_31(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            str_0 = 'PV'
            group_0 = module_0.Group(str_0)
            var_0 = group_0.get_vars()
            bool_0 = False
            var_1 = group_0.deserialize(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
