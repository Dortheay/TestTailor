import unittest
import timeout_decorator
import ansible.playbook.base as module_0

class Test_Base_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            field_attribute_base_0 = module_0.FieldAttributeBase()
            var_0 = field_attribute_base_0.get_loader()
            bytes_0 = b'Pr\x89\xc6'
            list_0 = [var_0, bytes_0]
            var_1 = field_attribute_base_0.load_data(bytes_0, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
