import unittest
import timeout_decorator
import ansible.playbook.base as module_0

class Test_Base_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            field_attribute_base_0 = module_0.FieldAttributeBase()
            base_0 = module_0.Base()
            var_0 = base_0.get_dep_chain()
            var_1 = field_attribute_base_0.validate()
            base_1 = module_0.Base()
            var_2 = base_1.get_dep_chain()
            dict_0 = {}
            var_3 = field_attribute_base_0.deserialize(dict_0)
            var_4 = field_attribute_base_0.validate()
            base_2 = module_0.Base()
            var_5 = base_2.get_path()
            field_attribute_base_1 = module_0.FieldAttributeBase()
            bool_0 = True
            var_6 = field_attribute_base_1.dump_me(bool_0)
            var_7 = field_attribute_base_0.deserialize(field_attribute_base_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
