import unittest
import timeout_decorator
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

class Test_Host_16(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        set_0 = set()
        list_0 = []
        host_0 = module_0.Host(list_0)
        var_0 = host_0.populate_ancestors()
        var_1 = host_0.populate_ancestors(set_0)
        bool_0 = False
        dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
        host_1 = module_0.Host(dict_0)
        int_0 = -3365
        bytes_0 = b'\x9b\x07\x99\xd0B\x99\x13R'
        bool_1 = True
        var_2 = host_1.set_variable(bool_1, list_0)
        float_0 = -117.033
        bytes_1 = b"\x03\x9b\x1eP\xbd'-"
        tuple_0 = (int_0, bytes_0, float_0, bytes_1)
        host_2 = module_0.Host(tuple_0)
        var_3 = host_1.__repr__()

if __name__ == "__main__":
    unittest.main()
