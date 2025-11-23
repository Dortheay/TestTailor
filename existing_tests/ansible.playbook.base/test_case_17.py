import unittest
import timeout_decorator
import ansible.playbook.base as module_0

class Test_Base_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            field_attribute_base_0 = module_0.FieldAttributeBase()
            field_attribute_base_1 = module_0.FieldAttributeBase()
            var_0 = field_attribute_base_0.copy()
            str_0 = 'XQ&\rz[-:@[- L;J&'
            var_1 = field_attribute_base_0.from_attrs(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
