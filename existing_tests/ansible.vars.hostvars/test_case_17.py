import unittest
import timeout_decorator
import ansible.vars.hostvars as module_0

class Test_Hostvars_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_14(self):
        try:
            bytes_0 = b'\x97]'
            int_0 = 32
            host_vars_vars_0 = module_0.HostVarsVars(bytes_0, int_0)
            host_vars_0 = module_0.HostVars(host_vars_vars_0, host_vars_vars_0, int_0)
            int_1 = -2407
            bytes_1 = b'\xed\xbc\xc6\xf5\xbf['
            var_0 = host_vars_0.set_host_variable(bytes_0, int_1, bytes_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
