import unittest
import timeout_decorator
import ansible.playbook.base as module_0

class Test_Base_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            field_attribute_base_0 = module_0.FieldAttributeBase()
            list_0 = [field_attribute_base_0]
            float_0 = -584.38104
            str_0 = ''
            list_1 = [float_0, str_0, list_0, list_0]
            var_0 = field_attribute_base_0.get_validated_value(list_0, float_0, str_0, list_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
