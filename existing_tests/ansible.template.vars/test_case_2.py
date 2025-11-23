import unittest
import timeout_decorator
import ansible.template.vars as module_0

class Test_Vars_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        bytes_0 = b'\xe62\xba1s\xe5/\xba\xb2\x13\xa9&\xdf|\r\x1dZ\xb9\xea'
        dict_0 = {bytes_0: bytes_0, bytes_0: bytes_0, bytes_0: bytes_0}
        dict_1 = {bytes_0: bytes_0}
        str_0 = 'F'
        ansible_j2_vars_0 = module_0.AnsibleJ2Vars(dict_1, str_0)
        bool_0 = False
        ansible_j2_vars_1 = module_0.AnsibleJ2Vars(ansible_j2_vars_0, bool_0)
        var_0 = ansible_j2_vars_1.add_locals(dict_0)

if __name__ == "__main__":
    unittest.main()
