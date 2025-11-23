import unittest
import timeout_decorator
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

class Test_Host_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        try:
            int_0 = -1649
            dict_0 = {}
            list_0 = [dict_0, int_0, int_0]
            tuple_0 = ()
            tuple_1 = (list_0, tuple_0)
            host_0 = module_0.Host(dict_0)
            var_0 = host_0.__ne__(tuple_1)
            host_1 = module_0.Host(dict_0)
            var_1 = host_1.add_group(int_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
