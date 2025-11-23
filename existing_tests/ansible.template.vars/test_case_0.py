import unittest
import timeout_decorator
import ansible.template.vars as module_0

class Test_Vars_1(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = 'Tr1U4b\nHF'
        ansible_j2_vars_0 = module_0.AnsibleJ2Vars(str_0, str_0)

if __name__ == "__main__":
    unittest.main()
