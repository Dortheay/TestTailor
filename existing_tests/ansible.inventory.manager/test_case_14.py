import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_15(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_2(self):
        float_0 = -725.732
        list_0 = [float_0, float_0]
        float_1 = -1069.0745
        set_0 = {float_1}
        inventory_manager_0 = module_0.InventoryManager(set_0)
        var_0 = inventory_manager_0.get_groups_dict()
        var_1 = inventory_manager_0.subset(list_0)

if __name__ == "__main__":
    unittest.main()
