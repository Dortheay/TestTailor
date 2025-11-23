import unittest
import timeout_decorator
import ansible.vars.hostvars as module_0

class Test_Hostvars_9(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            int_0 = -1573
            tuple_0 = (int_0,)
            str_0 = '%uk'
            bool_0 = True
            host_vars_vars_0 = module_0.HostVarsVars(str_0, bool_0)
            tuple_1 = ()
            list_0 = [tuple_1]
            host_vars_vars_1 = module_0.HostVarsVars(host_vars_vars_0, list_0)
            list_1 = []
            host_vars_vars_2 = module_0.HostVarsVars(host_vars_vars_1, list_1)
            var_0 = host_vars_vars_2.__contains__(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
