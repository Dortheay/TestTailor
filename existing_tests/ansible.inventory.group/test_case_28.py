import unittest
import timeout_decorator
import ansible.inventory.group as module_0

class Test_Group_29(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            group_0 = module_0.Group()
            var_0 = group_0.get_name()
            var_1 = group_0.get_descendants()
            var_2 = group_0.remove_host(group_0)
            group_1 = module_0.Group()
            var_3 = group_1.get_descendants()
            var_4 = group_0.get_hosts()
            var_5 = group_0.remove_host(group_0)
            var_6 = group_0.__str__()
            var_7 = group_1.__getstate__()
            group_2 = module_0.Group()
            var_8 = group_0.__str__()
            var_9 = group_2.serialize()
            var_10 = group_1.add_child_group(group_0)
            str_0 = ''
            str_1 = 'vz$\\0A=>7qJ@'
            str_2 = 'LDk8Xz60N*6I..Y='
            dict_0 = {str_2: var_0}
            dict_1 = {str_0: var_8, str_1: dict_0}
            var_11 = module_0.to_safe_group_name(dict_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
