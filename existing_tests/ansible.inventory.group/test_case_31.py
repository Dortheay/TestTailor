import unittest
import timeout_decorator
import ansible.inventory.group as module_0

class Test_Group_32(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        try:
            str_0 = 'parent_group'
            group_0 = module_0.Group(str_0)
            str_1 = 'child_group'
            group_1 = module_0.Group(str_1)
            var_0 = group_0.add_child_group(group_1)
            var_1 = group_1.add_child_group(group_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
