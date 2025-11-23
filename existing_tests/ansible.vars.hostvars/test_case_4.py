import unittest
import timeout_decorator
import ansible.vars.hostvars as module_0

class Test_Hostvars_5(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            float_0 = 0.001
            tuple_0 = (float_0,)
            bool_0 = True
            dict_0 = {bool_0: float_0, float_0: bool_0}
            host_vars_vars_0 = module_0.HostVarsVars(dict_0, dict_0)
            host_vars_0 = module_0.HostVars(bool_0, host_vars_vars_0, float_0)
            var_0 = host_vars_0.raw_get(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
