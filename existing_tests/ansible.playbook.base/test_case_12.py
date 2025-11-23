import unittest
import timeout_decorator
import ansible.playbook.base as module_0

class Test_Base_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_12(self):
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.squash()
        var_1 = field_attribute_base_0.squash()
        var_2 = field_attribute_base_0.get_loader()
        var_3 = field_attribute_base_0.get_variable_manager()
        var_4 = field_attribute_base_0.copy()

if __name__ == "__main__":
    unittest.main()
