import unittest
import timeout_decorator
import ansible.vars.hostvars as module_0

class Test_Hostvars_13(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_9(self):
        try:
            bytes_0 = b'\x14-\x08\xd6M\xe4\xb4\xe8\xc7\x0b@\xb2Q@\x1c\x04'
            int_0 = 32
            host_vars_vars_0 = module_0.HostVarsVars(bytes_0, int_0)
            host_vars_0 = module_0.HostVars(host_vars_vars_0, host_vars_vars_0, int_0)
            str_0 = '/usr/local/share/certs'
            var_0 = host_vars_0.set_variable_manager(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
