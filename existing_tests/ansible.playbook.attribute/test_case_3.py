import unittest
import timeout_decorator
import ansible.playbook.attribute as module_0

class Test_Attribute_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            float_0 = 1502.3049569710333
            bytes_0 = b'\xd95'
            tuple_0 = (float_0,)
            list_0 = [bytes_0, tuple_0]
            bool_0 = True
            str_0 = 'weekly'
            attribute_0 = module_0.Attribute(bool_0, str_0)
            var_0 = attribute_0.__gt__(list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
