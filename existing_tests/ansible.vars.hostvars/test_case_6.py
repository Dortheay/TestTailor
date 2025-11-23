import unittest
import timeout_decorator
import ansible.vars.hostvars as module_0

class Test_Hostvars_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            bytes_0 = b'\x97]'
            bool_0 = False
            int_0 = 32
            host_vars_vars_0 = module_0.HostVarsVars(bytes_0, int_0)
            host_vars_0 = module_0.HostVars(host_vars_vars_0, host_vars_vars_0, int_0)
            var_0 = host_vars_0.__deepcopy__(bool_0)
            int_1 = 36
            list_0 = [int_1, int_1]
            host_vars_1 = module_0.HostVars(bool_0, int_1, list_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
