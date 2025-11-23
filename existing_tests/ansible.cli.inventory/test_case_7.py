import unittest
import timeout_decorator
import ansible.cli.inventory as module_0

class Test_Inventory_8(unittest.TestCase):
    @timeout_decorator.timeout(5)
    def test_case_0(self):
        str_0 = 'u4zY;@eL]#p7\x0bN^G +$j'
        inventory_c_l_i_0 = module_0.InventoryCLI(str_0)

if __name__ == "__main__":
    unittest.main()
