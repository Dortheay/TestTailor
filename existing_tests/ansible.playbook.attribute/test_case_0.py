import unittest
import timeout_decorator
import ansible.playbook.attribute as module_0

class Test_Attribute_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            bytes_0 = b'\xf7\xde\xeei"\xd6\xa5\x98'
            set_0 = {bytes_0, bytes_0}
            bool_0 = False
            str_0 = 'run_state'
            attribute_0 = module_0.Attribute(bool_0, str_0)
            var_0 = attribute_0.__eq__(set_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
