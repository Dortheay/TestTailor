import unittest
import timeout_decorator
import ansible.inventory.host as module_0
import ansible.inventory.group as module_1

class Test_Host_20(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_10(self):
        bool_0 = False
        host_0 = module_0.Host()
        var_0 = host_0.populate_ancestors()
        var_1 = host_0.__str__()
        host_1 = module_0.Host(bool_0)
        bytes_0 = b'\x81\x01\xff\xcf\x1d\xca\x0f^\xab\xd9=\xacUwJ~'
        var_2 = host_1.populate_ancestors()
        list_0 = []
        tuple_0 = (list_0,)
        var_3 = host_1.__eq__(tuple_0)
        var_4 = host_0.get_groups()
        var_5 = host_0.__hash__()
        var_6 = host_0.__hash__()
        var_7 = host_1.__getstate__()
        host_2 = module_0.Host(tuple_0)
        var_8 = host_2.__eq__(host_0)
        var_9 = host_0.remove_group(bytes_0)
        str_0 = 'P8'
        var_10 = host_0.set_variable(bool_0, str_0)

if __name__ == "__main__":
    unittest.main()
