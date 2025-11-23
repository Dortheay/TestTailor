import unittest
import timeout_decorator
import ansible.vars.hostvars as module_0

class Test_Hostvars_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        try:
            bool_0 = True
            str_0 = 'TbgpbM*%c6'
            float_0 = -531.0
            bytes_0 = None
            dict_0 = {str_0: bool_0, bytes_0: bool_0}
            host_vars_vars_0 = module_0.HostVarsVars(float_0, dict_0)
            tuple_0 = ()
            host_vars_0 = module_0.HostVars(str_0, host_vars_vars_0, tuple_0)
            str_1 = 'M\x0cO>eI\r[AcAe|'
            host_vars_1 = module_0.HostVars(host_vars_0, host_vars_0, str_1)
            var_0 = host_vars_1.__contains__(bool_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
