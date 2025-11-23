import unittest
import timeout_decorator
import ansible.inventory.group as module_0

class Test_Group_30(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            group_0 = module_0.Group()
            group_1 = module_0.Group()
            var_0 = group_0.get_hosts()
            var_1 = group_0.remove_host(group_0)
            var_2 = group_1.__getstate__()
            group_2 = module_0.Group()
            str_0 = '\n^'
            var_3 = group_1.set_variable(group_2, str_0)
            var_4 = group_2.serialize()
            var_5 = group_1.add_child_group(group_0)
            var_6 = group_1.get_hosts()
            group_3 = module_0.Group()
            var_7 = group_3.deserialize(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
