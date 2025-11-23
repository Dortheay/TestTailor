import unittest
import timeout_decorator
import ansible.playbook.base as module_0

class Test_Base_17(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            field_attribute_base_0 = module_0.FieldAttributeBase()
            var_0 = field_attribute_base_0.get_ds()
            base_0 = module_0.Base()
            var_1 = field_attribute_base_0.post_validate(base_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
