import unittest
import timeout_decorator
import ansible.playbook.base as module_0

class Test_Base_22(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            field_attribute_base_0 = module_0.FieldAttributeBase()
            var_0 = field_attribute_base_0.copy()
            base_0 = module_0.Base()
            var_1 = base_0.get_dep_chain()
            var_2 = base_0.get_search_path()
            var_3 = base_0.get_dep_chain()
            field_attribute_base_1 = module_0.FieldAttributeBase()
            float_0 = None
            var_4 = field_attribute_base_1.preprocess_data(float_0)
            var_5 = field_attribute_base_0.serialize()
            var_6 = base_0.get_search_path()
            var_7 = base_0.get_path()
            var_8 = base_0.get_dep_chain()
            field_attribute_base_2 = module_0.FieldAttributeBase()
            int_0 = -2264
            var_9 = field_attribute_base_2.load_data(base_0, base_0, int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
