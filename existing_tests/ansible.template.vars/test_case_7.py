import unittest
import timeout_decorator
import ansible.template.vars as module_0

class Test_Vars_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_4(self):
        try:
            int_0 = 63
            str_0 = 'TrU4b\nHF'
            ansible_j2_vars_0 = module_0.AnsibleJ2Vars(str_0, str_0)
            var_0 = ansible_j2_vars_0.__getitem__(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
