import unittest
import timeout_decorator
import ansible.playbook.base as module_0

class Test_Base_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.validate()
        dict_0 = {}
        var_1 = field_attribute_base_0.deserialize(dict_0)
        var_2 = field_attribute_base_0.validate()
        var_3 = field_attribute_base_0.validate()
        var_4 = field_attribute_base_0.dump_attrs()
        var_5 = field_attribute_base_0.copy()

if __name__ == "__main__":
    unittest.main()
