import unittest
import timeout_decorator
import ansible.inventory.group as module_0

class Test_Group_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        group_0 = module_0.Group()
        str_0 = 'a.[;>`s'
        float_0 = 306.1
        set_0 = {str_0}
        var_0 = group_0.set_variable(float_0, set_0)
        var_1 = module_0.to_safe_group_name(str_0, float_0)
        group_1 = module_0.Group()
        var_2 = group_0.get_hosts()
        var_3 = group_1.__str__()
        var_4 = group_1.__getstate__()
        var_5 = group_0.__str__()
        str_1 = '\n^'
        var_6 = group_1.set_variable(group_0, str_1)
        var_7 = group_1.serialize()
        var_8 = group_1.add_child_group(group_0)
        var_9 = group_1.get_hosts()
        var_10 = group_0.__getstate__()

if __name__ == "__main__":
    unittest.main()
