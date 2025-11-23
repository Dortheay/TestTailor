import unittest
import timeout_decorator
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

class Test_Host_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            bool_0 = True
            dict_0 = {bool_0: bool_0, bool_0: bool_0}
            str_0 = '-mR/ctm1~?Ah('
            host_0 = module_0.Host()
            var_0 = host_0.get_name()
            host_1 = module_0.Host(str_0)
            var_1 = host_1.deserialize(dict_0)
            var_2 = host_0.populate_ancestors(str_0)
            host_2 = module_0.Host()
            var_3 = host_2.__str__()
            str_1 = '_ownload_Grl'
            int_0 = -377
            set_0 = {str_1, host_2, str_1, int_0}
            tuple_0 = None
            var_4 = host_1.__getstate__()
            var_5 = host_2.__repr__()
            host_3 = module_0.Host()
            bool_1 = True
            int_1 = 471
            var_6 = host_0.set_variable(bool_1, int_1)
            int_2 = 32603
            var_7 = host_2.set_variable(int_2, int_2)
            host_4 = module_0.Host(host_1)
            var_8 = host_3.remove_group(tuple_0)
            var_9 = host_3.get_groups()
            host_5 = module_0.Host(set_0)
            var_10 = host_0.populate_ancestors()
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
