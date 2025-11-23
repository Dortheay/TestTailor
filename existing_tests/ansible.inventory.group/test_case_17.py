import unittest
import timeout_decorator
import ansible.inventory.group as module_0

class Test_Group_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_17(self):
        group_0 = module_0.Group()
        var_0 = group_0.get_name()
        str_0 = 'a.[;>`s'
        float_0 = 306.1
        var_1 = group_0.__str__()
        var_2 = module_0.to_safe_group_name(str_0, float_0)
        group_1 = module_0.Group()
        var_3 = group_1.get_descendants()
        var_4 = group_0.get_hosts()
        var_5 = group_0.remove_host(group_0)
        var_6 = group_0.__str__()
        var_7 = group_1.__getstate__()
        group_2 = module_0.Group()
        var_8 = group_0.__str__()
        str_1 = '\n^'
        var_9 = group_1.set_variable(group_2, str_1)
        var_10 = group_2.serialize()
        var_11 = group_1.add_child_group(group_0)
        var_12 = group_1.get_hosts()
        group_3 = module_0.Group()
        var_13 = group_2.add_child_group(group_0)

if __name__ == "__main__":
    unittest.main()
