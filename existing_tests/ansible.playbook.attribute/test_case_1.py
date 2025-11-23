import unittest
import timeout_decorator
import ansible.playbook.attribute as module_0

class Test_Attribute_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = 740.19
            bool_0 = True
            attribute_0 = module_0.Attribute(bool_0)
            var_0 = attribute_0.__ne__(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
