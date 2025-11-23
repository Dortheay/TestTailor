import unittest
import timeout_decorator
import ansible.playbook.base as module_0

class Test_Base_23(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            base_0 = module_0.Base()
            field_attribute_base_0 = module_0.FieldAttributeBase()
            var_0 = field_attribute_base_0.get_ds()
            base_1 = module_0.Base()
            var_1 = base_1.get_dep_chain()
            var_2 = field_attribute_base_0.validate()
            var_3 = base_1.get_path()
            field_attribute_base_1 = module_0.FieldAttributeBase()
            var_4 = base_1.get_dep_chain()
            field_attribute_base_2 = module_0.FieldAttributeBase()
            complex_0 = None
            tuple_0 = None
            var_5 = field_attribute_base_2.load_data(complex_0, tuple_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
