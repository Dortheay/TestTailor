import unittest
import timeout_decorator
import ansible.playbook.attribute as module_0

class Test_Attribute_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            float_0 = 1454.3172
            str_0 = 's#t'
            attribute_0 = module_0.Attribute(str_0, float_0, str_0)
            tuple_0 = ()
            bool_0 = False
            attribute_1 = module_0.Attribute(tuple_0, bool_0)
            var_0 = attribute_0.__ge__(attribute_1)
            var_1 = attribute_0.__lt__(float_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
