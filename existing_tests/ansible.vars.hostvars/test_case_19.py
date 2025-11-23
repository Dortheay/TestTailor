import unittest
import timeout_decorator
import ansible.vars.hostvars as module_0

class Test_Hostvars_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_16(self):
        try:
            str_0 = 'var2'
            var_0 = None
            host_vars_vars_0 = module_0.HostVarsVars(str_0, var_0)
            var_1 = iter(host_vars_vars_0)
            var_2 = list(var_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
