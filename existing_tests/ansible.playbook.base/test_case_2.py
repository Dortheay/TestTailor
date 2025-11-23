import unittest
import timeout_decorator
import ansible.playbook.base as module_0

class Test_Base_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        field_attribute_base_0 = module_0.FieldAttributeBase()
        list_0 = [field_attribute_base_0, field_attribute_base_0]
        var_0 = field_attribute_base_0.validate(list_0)
        var_1 = field_attribute_base_0.dump_me()
        var_2 = field_attribute_base_0.get_variable_manager()

if __name__ == "__main__":
    unittest.main()
