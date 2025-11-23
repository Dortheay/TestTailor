import unittest
import timeout_decorator
import ansible.vars.hostvars as module_0

class Test_Hostvars_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        str_0 = 'uid=%s'
        dict_0 = {}
        host_vars_vars_0 = module_0.HostVarsVars(str_0, dict_0)
        var_0 = host_vars_vars_0.__repr__()

if __name__ == "__main__":
    unittest.main()
