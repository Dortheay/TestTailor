import unittest
import timeout_decorator
import ansible.plugins.vars.host_group_vars as module_0
import ansible.inventory.host as module_1

class Test_Host_group_vars_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        int_0 = 2049
        bool_0 = False
        float_0 = 2408.94889
        vars_module_0 = module_0.VarsModule()
        dict_0 = {bool_0: int_0, bool_0: bool_0, vars_module_0: float_0, vars_module_0: float_0}
        bytes_0 = b'\x11iUT\xae\x10\xaa'
        list_0 = []
        var_0 = vars_module_0.get_vars(dict_0, bytes_0, list_0)

if __name__ == "__main__":
    unittest.main()
