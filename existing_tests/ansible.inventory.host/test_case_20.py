import unittest
import timeout_decorator
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

class Test_Host_21(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_11(self):
        bool_0 = True
        dict_0 = {bool_0: bool_0, bool_0: bool_0}
        host_0 = module_0.Host()
        var_0 = host_0.__str__()
        str_0 = 'download_url'
        int_0 = -354
        set_0 = {str_0, host_0, str_0, int_0}
        var_1 = host_0.__getstate__()
        var_2 = host_0.__repr__()
        host_1 = module_0.Host()
        int_1 = 471
        var_3 = host_0.set_variable(bool_0, int_1)
        float_0 = -775.86
        int_2 = 32603
        var_4 = host_0.set_variable(int_2, int_2)
        host_2 = module_0.Host(float_0)
        host_3 = module_0.Host()
        var_5 = host_3.remove_group(dict_0)
        var_6 = host_3.get_groups()
        var_7 = host_2.populate_ancestors()
        var_8 = host_0.set_variable(bool_0, set_0)
        host_4 = module_0.Host()

if __name__ == "__main__":
    unittest.main()
