import unittest
import timeout_decorator
import ansible.inventory.group as module_0

class Test_Group_28(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            group_0 = module_0.Group()
            var_0 = group_0.remove_host(group_0)
            var_1 = group_0.__str__()
            var_2 = group_0.__getstate__()
            group_1 = module_0.Group()
            var_3 = group_1.__str__()
            var_4 = group_0.add_child_group(group_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
