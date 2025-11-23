import unittest
import timeout_decorator
import ansible.playbook.attribute as module_0

class Test_Attribute_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'adv'
        set_0 = {str_0, str_0}
        bytes_0 = b'y$\xa8\xa49\xec\xf8U\xd3B\xc1\x14\x91\xe0^\x16\rv'
        attribute_0 = module_0.Attribute(set_0, bytes_0)
        int_0 = 36
        bool_0 = False
        attribute_1 = module_0.Attribute(int_0, bool_0)
        var_0 = attribute_1.__le__(attribute_0)
        field_attribute_0 = module_0.FieldAttribute(str_0)

if __name__ == "__main__":
    unittest.main()
