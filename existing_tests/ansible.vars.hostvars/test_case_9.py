import unittest
import timeout_decorator
import ansible.vars.hostvars as module_0

class Test_Hostvars_10(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            bytes_0 = b'\xda\xc7\xa6\x9c\xb8\x9d\x80z\xe7\xb0,\xf5\x9f\x90\x0e'
            str_0 = 'l'
            str_1 = ''
            set_0 = {bytes_0}
            bool_0 = True
            host_vars_vars_0 = module_0.HostVarsVars(set_0, bool_0)
            tuple_0 = (host_vars_vars_0, set_0)
            host_vars_vars_1 = module_0.HostVarsVars(str_1, tuple_0)
            tuple_1 = (host_vars_vars_1,)
            host_vars_vars_2 = module_0.HostVarsVars(str_0, tuple_1)
            int_0 = 1369
            bytes_1 = b'\x84\x93\x0e\xd35\xd4\xb4\xe0\x9fU\t\x17I'
            str_2 = 'XDJ?&.=zfm|S'
            host_vars_vars_3 = module_0.HostVarsVars(bytes_1, str_2)
            set_1 = {bytes_1}
            host_vars_0 = module_0.HostVars(int_0, host_vars_vars_3, set_1)
            var_0 = host_vars_0.set_host_facts(bytes_0, host_vars_vars_2)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
