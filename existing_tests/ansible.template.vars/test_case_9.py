import unittest
import timeout_decorator
import ansible.template.vars as module_0

class Test_Vars_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            bytes_0 = b'\xf8\xaf#\x01\xcc\x9cJ\x8b*\xb8\xee\xbb'
            bool_0 = True
            float_0 = -2116.9395
            bool_1 = True
            dict_0 = {bytes_0: float_0, float_0: bool_0, bool_1: bytes_0}
            ansible_j2_vars_0 = module_0.AnsibleJ2Vars(bytes_0, bool_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
