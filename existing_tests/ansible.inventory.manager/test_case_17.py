import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_18(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        str_0 = '\n    This is a generic TCP Connection Info strategy class that relies\n    on the psutil module, which is not ideal for targets, but necessary\n    for cross platform support.\n\n    A subclass may wish to override some or all of these methods.\n      - _get_exclude_ips()\n      - get_active_connections()\n\n    All subclasses MUST define platform and distribution (which may be None).\n    '
        str_1 = 'shK&#\\w+3BE'
        list_0 = [str_1, str_1, str_1]
        inventory_manager_0 = module_0.InventoryManager(str_1, list_0)
        var_0 = inventory_manager_0.parse_source(str_0)

if __name__ == "__main__":
    unittest.main()
