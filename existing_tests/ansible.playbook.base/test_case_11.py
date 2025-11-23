import unittest
import timeout_decorator
import ansible.playbook.base as module_0

class Test_Base_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        str_0 = "eIDDwv' "
        dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
        field_attribute_base_0 = module_0.FieldAttributeBase()
        var_0 = field_attribute_base_0.validate(dict_0)
        field_attribute_base_1 = module_0.FieldAttributeBase()
        list_0 = [dict_0, field_attribute_base_0, field_attribute_base_1]
        var_1 = field_attribute_base_1.serialize()
        var_2 = field_attribute_base_1.serialize()
        var_3 = field_attribute_base_0.dump_me()
        var_4 = field_attribute_base_0.get_loader()
        tuple_0 = ()
        list_1 = [list_0]
        var_5 = field_attribute_base_0.load_data(tuple_0, list_1)
        field_attribute_base_2 = module_0.FieldAttributeBase()

if __name__ == "__main__":
    unittest.main()
