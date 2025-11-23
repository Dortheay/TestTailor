import unittest
import timeout_decorator
import ansible.inventory.group as module_0

class Test_Group_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        str_0 = 'Qarenu;_group'
        group_0 = module_0.Group(str_0)
        group_1 = module_0.Group(str_0)
        var_0 = group_0.add_child_group(group_1)

if __name__ == "__main__":
    unittest.main()
