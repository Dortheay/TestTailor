import unittest
import timeout_decorator
import ansible.vars.hostvars as module_0

class Test_Hostvars_12(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_8(self):
        try:
            bool_0 = True
            bool_1 = False
            str_0 = 'a'
            int_0 = 1134
            bytes_0 = b''
            host_vars_vars_0 = module_0.HostVarsVars(bytes_0, bool_0)
            str_1 = ''
            host_vars_vars_1 = module_0.HostVarsVars(host_vars_vars_0, str_1)
            str_2 = 'I \n\x0cdee#YU7zO_R'
            host_vars_0 = module_0.HostVars(int_0, host_vars_vars_1, str_2)
            var_0 = host_vars_0.set_nonpersistent_facts(bool_1, str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
