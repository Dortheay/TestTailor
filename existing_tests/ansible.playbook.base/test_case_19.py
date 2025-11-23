import unittest
import timeout_decorator
import ansible.playbook.base as module_0

class Test_Base_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            bytes_0 = b' \xe1\x9e\xc3\xb6NL\xd4Ex\xc2\x8ei'
            field_attribute_base_0 = module_0.FieldAttributeBase()
            var_0 = field_attribute_base_0.deserialize(bytes_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
