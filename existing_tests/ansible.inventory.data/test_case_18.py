import unittest
import timeout_decorator
import ansible.inventory.data as module_0
import ansible.inventory.group as module_1

class Test_Data_19(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_5(self):
        try:
            str_0 = '_vdEWPE^C'
            tuple_0 = (str_0, str_0)
            inventory_data_0 = module_0.InventoryData()
            var_0 = inventory_data_0.add_host(str_0, tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
