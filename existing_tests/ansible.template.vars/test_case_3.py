import unittest
import timeout_decorator
import ansible.template.vars as module_0

class Test_Vars_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        try:
            int_0 = 4309
            dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0, int_0: int_0}
            bytes_0 = b'\xd5\x90\x017}r\x92\x84[UV\xd6b\xae'
            ansible_j2_vars_0 = module_0.AnsibleJ2Vars(dict_0, bytes_0, dict_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
