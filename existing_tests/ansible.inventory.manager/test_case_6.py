import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_7(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_6(self):
        try:
            tuple_0 = ()
            bytes_0 = b'V\x05\xc4\x86Z\x81\xf6\xff\xa0SE\xb1\x07\xaf\x9a"'
            float_0 = -126.13
            set_0 = None
            str_0 = 'Z(p|\\'
            inventory_manager_0 = module_0.InventoryManager(str_0)
            var_0 = inventory_manager_0.restrict_to_hosts(set_0)
            set_1 = {tuple_0, float_0, bytes_0, float_0, tuple_0, inventory_manager_0, tuple_0}
            inventory_manager_1 = module_0.InventoryManager(float_0, set_1)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
