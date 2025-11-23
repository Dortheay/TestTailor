import unittest
import timeout_decorator
import ansible.playbook.attribute as module_0

class Test_Attribute_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'list'
        bool_0 = True
        var_0 = []
        var_1 = lambda : var_0
        bool_1 = True
        str_1 = 'string'
        int_0 = 5
        var_2 = None
        bool_2 = False
        bool_3 = False
        str_2 = 'test_alias'
        bool_4 = True
        bool_5 = False
        bool_6 = False
        field_attribute_0 = module_0.FieldAttribute(str_0, bool_0, var_1, bool_1, str_1, int_0, var_2, bool_2, bool_3, str_2, bool_4, bool_5, bool_6)

if __name__ == "__main__":
    unittest.main()
