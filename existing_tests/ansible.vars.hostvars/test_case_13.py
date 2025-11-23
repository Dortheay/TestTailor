import unittest
import timeout_decorator
import ansible.vars.hostvars as module_0

class Test_Hostvars_14(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        try:
            bytes_0 = b'\x97]'
            bool_0 = False
            int_0 = 32
            host_vars_vars_0 = module_0.HostVarsVars(bytes_0, int_0)
            host_vars_0 = module_0.HostVars(host_vars_vars_0, host_vars_vars_0, int_0)
            list_0 = []
            var_0 = host_vars_0.__setstate__(list_0)
            var_1 = host_vars_0.__deepcopy__(bool_0)
            str_0 = 'DRY RUN'
            var_2 = host_vars_0.set_inventory(str_0)
            var_3 = host_vars_0.__len__()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
