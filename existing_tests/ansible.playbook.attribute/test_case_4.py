import unittest
import timeout_decorator
import ansible.playbook.attribute as module_0

class Test_Attribute_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        bool_0 = True
        attribute_0 = module_0.Attribute(bool_0)

if __name__ == "__main__":
    unittest.main()
