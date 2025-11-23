import unittest
import timeout_decorator
import ansible.vars.hostvars as module_0

class Test_Hostvars_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        try:
            str_0 = 'AnsibleJ2Template'
            str_1 = '?[w2GY'
            str_2 = 'lH@'
            set_0 = None
            tuple_0 = None
            str_3 = '+'
            str_4 = '5%gz@es49a@CP.9'
            bool_0 = True
            bytes_0 = b'\x04\xff|'
            bytes_1 = b'w-\xfcN\xa9i\xa9l\r\xac'
            tuple_1 = (bytes_0, bytes_1)
            list_0 = [set_0, set_0]
            host_vars_vars_0 = module_0.HostVarsVars(list_0, set_0)
            dict_0 = {str_2: bytes_0, bool_0: str_1, bool_0: str_0}
            tuple_2 = (tuple_1, host_vars_vars_0, dict_0)
            host_vars_vars_1 = module_0.HostVarsVars(bool_0, tuple_2)
            host_vars_vars_2 = module_0.HostVarsVars(str_4, host_vars_vars_1)
            host_vars_0 = module_0.HostVars(str_3, host_vars_vars_2, list_0)
            var_0 = host_vars_0.__getitem__(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
