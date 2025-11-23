import unittest
import timeout_decorator
import ansible.playbook.base as module_0

class Test_Base_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        field_attribute_base_0 = module_0.FieldAttributeBase()

if __name__ == "__main__":
    unittest.main()
