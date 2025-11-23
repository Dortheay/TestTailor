import unittest
import timeout_decorator
import ansible.playbook.base as module_0

class Test_Base_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.squash()
        var_1 = field_attribute_base_0.get_loader()
        str_0 = 'QY'
        str_1 = '.o}g:`QR]2h5o[hqh|I'
        set_0 = set()
        dict_0 = {str_0: var_0, str_1: field_attribute_base_0, str_1: set_0, str_0: set_0}
        var_2 = field_attribute_base_0.from_attrs(dict_0)

if __name__ == "__main__":
    unittest.main()
