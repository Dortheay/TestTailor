import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_6(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = '.Htb?eY|ji'
            float_0 = 3444.37
            inventory_manager_0 = module_0.InventoryManager(float_0)
            var_0 = inventory_manager_0.restrict_to_hosts(str_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
