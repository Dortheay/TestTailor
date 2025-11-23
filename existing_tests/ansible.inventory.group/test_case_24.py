import unittest
import timeout_decorator
import ansible.inventory.group as module_0

class Test_Group_25(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            group_0 = module_0.Group()
            var_0 = group_0.get_vars()
            bool_0 = True
            var_1 = group_0.add_child_group(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
