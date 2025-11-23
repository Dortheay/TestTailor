import unittest
import timeout_decorator
import ansible.inventory.group as module_0

class Test_Group_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_13(self):
        str_0 = 'group$@name'
        str_1 = '_'
        var_0 = module_0.to_safe_group_name(str_0, str_1)
        str_2 = 'clean_group_name'
        var_1 = module_0.to_safe_group_name(str_2)
        str_3 = 'group!#name'
        str_4 = '_'
        var_2 = module_0.to_safe_group_name(str_3, str_4)
        str_5 = 'name&%test'
        str_6 = '-'
        bool_0 = True
        var_3 = module_0.to_safe_group_name(str_5, str_6, bool_0)

if __name__ == "__main__":
    unittest.main()
