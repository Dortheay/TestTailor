import unittest
import timeout_decorator
import ansible.inventory.group as module_0

class Test_Group_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        str_0 = 'vars'
        str_1 = 'depth'
        str_2 = 'hosts'
        str_3 = 'parent_groups'
        str_4 = 'test_group'
        str_5 = 'var1'
        str_6 = 'var2'
        str_7 = 'value1'
        str_8 = 'value2'
        str_9 = {str_5: str_7, str_6: str_8}
        int_0 = 3
        str_10 = 'host1'
        str_11 = 'host2'
        str_12 = [str_10, str_11]
        str_13 = 'parent_group'
        var_0 = {}
        int_1 = 2
        var_1 = []
        var_2 = []
        var_3 = {str_7: str_13, str_0: var_0, str_1: int_1, str_2: var_1, str_3: var_2}
        var_4 = [var_3]
        var_5 = {str_6: str_4, str_0: str_9, str_1: int_0, str_2: str_12, str_3: var_4}
        group_0 = module_0.Group()
        var_6 = group_0.deserialize(var_5)
        var_7 = group_0.parent_groups
        var_8 = len(var_7)

if __name__ == "__main__":
    unittest.main()
