import unittest
import timeout_decorator
import ansible.vars.hostvars as module_0

class Test_Hostvars_3(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        str_0 = 'var1'
        str_1 = 'var2'
        str_2 = 'var3'
        str_3 = 'value1'
        str_4 = 'value2'
        str_5 = 'value3'
        str_6 = {str_0: str_3, str_1: str_4, str_2: str_5}
        var_0 = None
        host_vars_vars_0 = module_0.HostVarsVars(str_6, var_0)
        var_1 = list(host_vars_vars_0)

if __name__ == "__main__":
    unittest.main()
