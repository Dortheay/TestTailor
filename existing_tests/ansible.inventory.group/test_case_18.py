import unittest
import timeout_decorator
import ansible.inventory.group as module_0

class Test_Group_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_18(self):
        str_0 = 'replacer'
        str_1 = 'invalid-group-name'
        str_2 = 'invalid_group_name'
        str_3 = 'another:group:name'
        str_4 = 'another-group-name'
        str_5 = 'valid_group_name'
        var_0 = str_0 == str_5
        var_1 = module_0.to_safe_group_name(str_1, str_2, str_3, str_4)

if __name__ == "__main__":
    unittest.main()
