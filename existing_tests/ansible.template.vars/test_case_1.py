import unittest
import timeout_decorator
import ansible.template.vars as module_0

class Test_Vars_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        ansible_j2_vars_0 = None
        bytes_0 = b'\x82h\xf9ey\xa5\x03nY\xec\x14\x9f\xdf\x90\xd6\xca\xaa\xf1\xeb'
        bytes_1 = b'\xa5\x99\xafP{A\x15Dn'
        str_0 = "@Y4o|'`hest"
        ansible_j2_vars_1 = module_0.AnsibleJ2Vars(bytes_0, bytes_1, str_0)
        float_0 = -3450.02
        ansible_j2_vars_2 = module_0.AnsibleJ2Vars(ansible_j2_vars_1, float_0)
        var_0 = ansible_j2_vars_2.add_locals(ansible_j2_vars_0)

if __name__ == "__main__":
    unittest.main()
