import unittest
import timeout_decorator
import ansible.playbook.base as module_0

class Test_Base_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            base_0 = module_0.Base()
            var_0 = base_0.get_dep_chain()
            var_1 = base_0.get_search_path()
            var_2 = base_0.get_dep_chain()
            field_attribute_base_0 = module_0.FieldAttributeBase()
            var_3 = field_attribute_base_0.preprocess_data(base_0)
            var_4 = field_attribute_base_0.serialize()
            var_5 = base_0.get_search_path()
            var_6 = base_0.get_path()
            var_7 = base_0.get_dep_chain()
            field_attribute_base_1 = module_0.FieldAttributeBase()
            bytes_0 = b'\x9c'
            var_8 = field_attribute_base_1.load_data(bytes_0, base_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
