import unittest
import timeout_decorator
import ansible.inventory.manager as module_0

class Test_Manager_4(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_3(self):
        try:
            bytes_0 = b'Z9\xb6v\xaa\xeb\xea\xba\xa5\xe0\x87'
            bool_0 = True
            dict_0 = {bytes_0: bytes_0, bytes_0: bool_0, bool_0: bool_0}
            bytes_1 = b"'"
            tuple_0 = (bytes_0, dict_0, bytes_1)
            bytes_2 = b''
            inventory_manager_0 = module_0.InventoryManager(bytes_2)
            var_0 = inventory_manager_0.add_group(tuple_0)
        except BaseException:
            pass

if __name__ == "__main__":
    unittest.main()
