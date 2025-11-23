import unittest
import timeout_decorator
import ansible.plugins.inventory.advanced_host_list as module_0

class Test_Advanced_host_list_2(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_1(self):
        inventory_module_0 = module_0.InventoryModule()
        str_0 = '/sys/class/fc_host/*/port_name'
        var_0 = inventory_module_0.verify_file(str_0)

if __name__ == "__main__":
    unittest.main()
