import unittest
import timeout_decorator
import ansible.vars.hostvars as module_0

class Test_Hostvars_11(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_7(self):
        try:
            bytes_0 = b'\x97]'
            int_0 = 33
            host_vars_vars_0 = module_0.HostVarsVars(bytes_0, int_0)
            host_vars_0 = module_0.HostVars(host_vars_vars_0, host_vars_vars_0, int_0)
            list_0 = []
            var_0 = host_vars_0.__setstate__(list_0)
            var_1 = host_vars_0.__len__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
