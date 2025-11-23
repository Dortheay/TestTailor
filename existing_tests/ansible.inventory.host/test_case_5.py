import unittest
import timeout_decorator
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

class Test_Host_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            bool_0 = True
            dict_0 = {bool_0: bool_0, bool_0: bool_0}
            str_0 = '-mR/ctm1~?Ah('
            host_0 = module_0.Host()
            var_0 = host_0.get_name()
            host_1 = module_0.Host(str_0)
            var_1 = host_1.deserialize(dict_0)
            host_2 = module_0.Host()
            var_2 = host_2.__str__()
            var_3 = host_1.__getstate__()
            var_4 = host_2.__repr__()
            host_3 = module_0.Host()
            list_0 = [var_1]
            var_5 = host_0.remove_group(list_0)
            float_0 = -936.232
            host_4 = module_0.Host(float_0)
            str_1 = '~5T|4&eYi?5+nb'
            var_6 = host_2.populate_ancestors(str_1)
            float_1 = 490.1441
            var_7 = host_3.deserialize(float_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
